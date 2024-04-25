from gurobipy import Model, GRB

# Create a new model
model = Model("integer_programming_example")

# Create integer variables
x = model.addVar(vtype=GRB.INTEGER, name="x")
y = model.addVar(vtype=GRB.INTEGER, name="y")

# Set the objective function
model.setObjective(2 * x + 3 * y, GRB.MAXIMIZE)

# Add constraints
model.addConstr(4 * x + 2 * y <= 12, "c1")
model.addConstr(3 * x + 3 * y <= 12, "c2")
model.addConstr(x >= 0, "c3")
model.addConstr(y >= 0, "c4")

# Optimize the model
model.optimize()

# Print the optimal solution
if model.status == GRB.OPTIMAL:
    print(f"Optimal solution found: x = {x.X}, y = {y.X}")
else:
    print("Optimal solution not found. Status:", model.status)
