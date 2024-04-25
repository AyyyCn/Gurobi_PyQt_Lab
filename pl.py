from gurobipy import Model, GRB

def lire_entiers(message, n):
    return [int(x) for x in input(message).strip().split()[:n]]

# Demande de données à l'utilisateur
n = int(input("Entrez le nombre de produits: "))
couts = lire_entiers("Entrez les coûts pour chaque produit, séparés par des espaces: ", n)
durees = lire_entiers("Entrez les durées pour chaque produit, séparés par des espaces: ", n)
profit_par_produit = lire_entiers("Entrez les profits pour chaque produit, séparés par des espaces: ", n)
ouvriers_necessaires = lire_entiers("Entrez le nombre d'ouvriers nécessaires par produit, séparés par des espaces: ", n)

limite_cout = int(input("Entrez la limite de coût totale: "))
limite_temps = int(input("Entrez la limite de temps total: "))
limite_ouvriers = int(input("Entrez le nombre total d'ouvriers disponibles: "))

# Créer le modèle
m = Model()

# Ajouter les variables
x = {i: m.addVar(vtype=GRB.INTEGER, name=f"x_{i}") for i in range(n)}

# Fonction objectif
m.setObjective(sum(profit_par_produit[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

# Ajouter les contraintes
m.addConstr(sum(couts[i] * x[i] for i in range(n)) <= limite_cout, "Contrainte_de_cout")
m.addConstr(sum(durees[i] * x[i] for i in range(n)) <= limite_temps, "Contrainte_de_temps")
m.addConstr(sum(ouvriers_necessaires[i] * x[i] for i in range(n)) <= limite_ouvriers, "Contrainte_de_ouvriers")

# Optimiser le modèle
m.optimize()

# Afficher les résultats
if m.status == GRB.OPTIMAL:
    print("Solution optimale trouvée:")
    for i in range(n):
        print(f"Produit {i}: Produire {x[i].X} unités")
else:
    print("Aucune solution optimale trouvée.")
