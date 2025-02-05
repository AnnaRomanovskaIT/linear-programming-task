import numpy as np
import matplotlib.pyplot as plt
from pulp import *

prob = LpProblem("LP_Problem", LpMinimize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

prob += 4*x1 - 5*x2 + 15, "Objective Function"

prob += 5*x1 + 3*x2 >= 23
prob += x1 + 5*x2 <= 31
prob += 3*x1 - x2 <= 13
prob += x1 - 2*x2 <= 2
prob.solve()

print("Status:", LpStatus[prob.status])
print("Optimal values:")
list=[]
for v in prob.variables():
    list.append(v.varValue);
    print(v.name, "=", v.varValue)
print("Optimal value of the objective function:", value(prob.objective))

constraints = [(5, 3, 23), (1, 5, 31), (3, -1, 13), (1, -2, 2)] 
c = np.array([4, -5])
x1 = np.linspace(-10, 10, 400)
plt.figure(figsize=(8, 6))
for constraint in constraints:
    x2 = (constraint[2] - constraint[0]*x1) / constraint[1]
    plt.plot(x1, x2, label=r"${}x_1 + {}x_2 \geq {}$".format(constraint[0], constraint[1], constraint[2]))
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')
plt.fill_between(x1, -10, 10, color='gray', alpha=0.3)
plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")
plt.xlim((-10, 10))
plt.ylim((-10, 10))
plt.legend()
plt.grid(True)
plt.title("Feasible Region")

plt.scatter(list[0], list[1], color='red', label='Мінімальна функція')
plt.legend()

plt.show()
