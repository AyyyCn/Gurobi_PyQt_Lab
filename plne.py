from gurobipy import Model, GRB, quicksum

def solve_backpack(names, values, constraints, limits):
    # Create a new model
    m = Model("integer_backpack")

    # Number of items
    n = len(values)

    # Create variables
    # x[i] is an integer, indicating how many units of item i are included in the knapsack
    x = m.addVars(n, vtype=GRB.INTEGER, name=["x_" + names[i] for i in range(n)])

    # Set objective: Maximize total value of the knapsack
    m.setObjective(quicksum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Adding constraints dynamically
    for i, constraint in enumerate(constraints):
        m.addConstr(quicksum(constraint[j] * x[j] for j in range(n - 1)) <= limits[i], f"constraint_{i}")

    # Optimize model
    m.optimize()

    # Display solution
    if m.status == GRB.OPTIMAL:
        results = {names[i]: x[i].X for i in range(n) if x[i].X > 0}
        total_value = sum(values[i] * x[i].X for i in range(n) if x[i].X > 0)
        return {"status": "Optimal", "results": results, "total_value": total_value}
    elif m.status == GRB.INFEASIBLE:
        return {"status": "Infeasible", "message": "No solution meets the constraints."}
    else:
        return {"status": "Error", "message": "Optimization did not solve successfully."}

"""
# Names of items
names = ['Item1', 'Item2', 'Item3', 'Item4']

# Values of each item (representing potential profit or utility)
values = [20, 30, 50, 10]

# Weights of each item (could represent physical weight, cost, or space taken)
weights = [15, 20, 30, 5]

# Constraints for a more complex scenario (e.g., volume and weight constraints)
constraints = [
    [10, 15, 25, 5],  # First constraint coefficients (e.g., volume constraint)
    [2, 3, 5, 1]       # Second constraint coefficients (e.g., weight constraint)
]

# Limits for each constraint (corresponding to the maximum allowed for each)
limits = [100, 40]  # Limits for the volume and weight constraints
result = solve_backpack(names, values, constraints, limits)
print(result)
"""