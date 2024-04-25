from gurobipy import Model, GRB

def lire_entiers(message, n):
    return [int(x) for x in input(message).strip().split()[:n]]

# Demande de données à l'utilisateur
n = int(input("Entrez le nombre de produits: "))

print("Entrez les coûts pour chaque produit, séparés par des espaces:")
couts = lire_entiers("Coûts: ", n)

print("Entrez les durées pour chaque produit, séparés par des espaces:")
durees = lire_entiers("Durées: ", n)

print("Entrez les profits pour chaque produit, séparés par des espaces:")
profit_par_produit = lire_entiers("Profits: ", n)

limite_cout = int(input("Entrez la limite de coût totale: "))
limite_temps = int(input("Entrez la limite de temps total: "))

# Créer le modèle
m = Model()

# Ajouter les variables
x = {i: m.addVar(vtype=GRB.INTEGER, name=f"x_{i}") for i in range(n)}

# Fonction objectif
m.setObjective(sum(profit_par_produit[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

# Ajouter les contraintes
m.addConstr(sum(couts[i] * x[i] for i in range(n)) <= limite_cout, "Contrainte_de_cout")
m.addConstr(sum(durees[i] * x[i] for i in range(n)) <= limite_temps, "Contrainte_de_temps")

# Optimiser le modèle
m.optimize()

# Afficher les résultats
if m.status == GRB.OPTIMAL:
    print("Solution optimale trouvée:")
    for i in range(n):
        print(f"Produit {i}: Produire {x[i].X} unités")
else:
    print("Aucune solution optimale trouvée.")
