from gurobipy import Model, GRB

def optimize_paint_mix(decision_vars, to_maximize, constraints, limits):
    m = Model()

    # Decision variables
    x = {var: m.addVar(name=f"x_{var}") for var in decision_vars}

    # Setting the objective function to maximize based on 'to_maximize' coefficients
    m.setObjective(sum(to_maximize[var] * x[var] for var in decision_vars), GRB.MAXIMIZE)

    # Applying constraints
    for i, constraint in enumerate(constraints):
        m.addConstr(sum(constraint[var] * x[var] for var in decision_vars) <= limits[i], f"constraint_{i}")

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



"""
Example running 
# Decision variables
decision_vars = ['A', 'B', 'C']

# Objective coefficients (profit per unit for each variable)
to_maximize = {
    'A': 3,  # Profit per unit for A
    'B': 5,  # Profit per unit for B
    'C': 2   # Profit per unit for C
}

# Constraints matrix (coefficients for constraints applied to each decision variable)
constraints = [
    {'A': 2, 'B': 1, 'C': 3},  # Coefficients for the first constraint (e.g., weight)
    {'A': 1, 'B': 3, 'C': 1}   # Coefficients for the second constraint (e.g., volume)
]

# Limits for each constraint
limits = [100, 90]  # e.g., 100 kg weight limit and 90 cubic meters volume limit
result = optimize_paint_mix(decision_vars, to_maximize, constraints, limits)
print(result)
"""