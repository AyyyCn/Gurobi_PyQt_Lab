from gurobipy import Model, GRB, quicksum

def solve_backpack(names, values, weights, capacity):
    # Create a new model
    m = Model("integer_backpack")

    # Number of items
    n = len(values)

    # Create variables
    # x[i] is an integer, indicating how many units of item i are included in the knapsack
    x = m.addVars(n, vtype=GRB.INTEGER, name=["x_" + names[i] for i in range(n)])

    # Set objective: Maximize total value of the knapsack
    m.setObjective(quicksum(values[i] * x[i] for i in range(n)), GRB.MAXIMIZE)

    # Add constraint: sum of weights of selected items should be less than or equal to capacity
    m.addConstr(quicksum(weights[i] * x[i] for i in range(n)) <= capacity, "capacity")

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



