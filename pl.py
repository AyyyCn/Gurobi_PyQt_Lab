from gurobipy import Model, GRB

def optimize_paint_mix(n, composants, couts, viscosite, densite, visco_max, max_garbage):
    m = Model()

    # Decision variables
    x = {comp: m.addVar(name=f"x_{comp}") for comp in composants}

    # Objective function: Minimize total cost
    m.setObjective(sum(couts[comp] * x[comp] for comp in composants), GRB.MAXIMIZE)

    # Viscosity constraints

    m.addConstr(sum(viscosite[comp] * x[comp] for comp in composants) <= visco_max, "max_viscosity")

    # Max garbage constraint
    m.addConstr(sum(densite[comp] * x[comp] for comp in composants) <= max_garbage, "max_garbage")



    # Optimize the model
    m.optimize()

    # Display results
    if m.status == GRB.OPTIMAL:
            results = {comp: x[comp].X for comp in composants}
            total_cost = sum(couts[comp] * x[comp].X for comp in composants)
            return {"status": "Optimal", "results": results, "total_cost": total_cost}
    elif m.status == GRB.INFEASIBLE:
        return {"status": "Infeasible", "message": "No solution meets the constraints."}
    else:
        return {"status": "Error", "message": "Optimization did not solve successfully."}
