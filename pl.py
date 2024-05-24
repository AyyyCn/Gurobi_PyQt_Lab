from gurobipy import Model, GRB, quicksum

def optimize_paint_mix(decision_vars, to_maximize, constraints, limits):
    m = Model()

    # Decision variables
    x = {var: m.addVar(name=f"x_{var}") for var in decision_vars}

    # Setting the objective function to maximize based on 'to_maximize' coefficients
    m.setObjective(sum(to_maximize[var] * x[var] for var in decision_vars), GRB.MAXIMIZE)

    # Applying constraints
    for i, constraint in enumerate(constraints):
        m.addConstr(quicksum(constraint[j] * x[j] for j in decision_vars) <= limits[i], f"constraint_{i}")

    # Optimize the model
    m.optimize()

    # Display results
    if m.status == GRB.OPTIMAL:
        results = {var: x[var].X for var in decision_vars}
        total_value = sum(to_maximize[var] * x[var].X for var in decision_vars)
        return {"status": "Optimal", "results": results, "total_value": total_value}
    elif m.status == GRB.INFEASIBLE:
        return {"status": "Infeasible", "message": "No solution meets the constraints."}
    else:
        return {"status": "Error", "message": "Optimization did not solve successfully."}
