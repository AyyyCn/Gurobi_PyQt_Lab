from gurobipy import Model, GRB

def main():
    # Données d'entrée
    produits = ['A', 'B', 'C']  # Exemple de produits
    demande = {'A': 100, 'B': 150, 'C': 200}  # Demande pour chaque produit
    cout_achat = {'A': 20, 'B': 30, 'C': 25}  # Coût d'achat par lot
    cout_stockage = {'A': 2, 'B': 1.5, 'C': 2.5}  # Coût de stockage par unité
    cout_fixe_commande = {'A': 5, 'B': 7, 'C': 6}  # Coût fixe par commande
    capacite_stockage = 500  # Capacité totale de stockage
    taille_lot = {'A': 50, 'B': 50, 'C': 50}  # Taille de chaque lot de produit

    # Créer le modèle
    m = Model()

    # Variables de décision
    x = {p: m.addVar(vtype=GRB.INTEGER, name=f"lots_{p}") for p in produits}
    y = {p: m.addVar(vtype=GRB.BINARY, name=f"commande_{p}") for p in produits}

    # Fonction objectif : Minimiser les coûts totaux
    m.setObjective(
        sum((cout_achat[p] * x[p] * taille_lot[p] + cout_fixe_commande[p] * y[p] + cout_stockage[p] * x[p] * taille_lot[p]) for p in produits),
        GRB.MINIMIZE
    )

    # Contraintes
    # Contrainte de demande
    for p in produits:
        m.addConstr(x[p] * taille_lot[p] >= demande[p], f"demande_{p}")
    
    # Contrainte de lien entre x et y
    for p in produits:
        m.addConstr(x[p] <= 1000 * y[p], f"lien_{p}")  # Assure que y_p = 1 si x_p > 0

    # Contrainte de capacité de stockage
    m.addConstr(sum(x[p] * taille_lot[p] for p in produits) <= capacite_stockage, "capacite_stockage")

    # Optimiser le modèle
    m.optimize()

    # Afficher les résultats
    if m.status == GRB.OPTIMAL:
        print("Solution optimale trouvée:")
        for p in produits:
            print(f"Produit {p}: Commander {x[p].X} lots, Commande active: {y[p].X}")
    else:
        print("Aucune solution optimale trouvée.")

if __name__ == "__main__":
    main()
