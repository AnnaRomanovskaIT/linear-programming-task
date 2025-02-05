# linear-programming-task
This repository contains all the code scripts I created to solve Linear Programming tasks using PuLP and NumPy.
____
`pr1_3` includes three functions, each designed to achieve specific objectives and display the most optimal result.

***Task 1 (Minimization & Maximization):***

Defines a linear programming problem to find both the minimum and maximum values of the objective function `2*x1 + 2*x2`

Constraints:

`x1 + x2 >= 2`

`x1 + x2 <= 5`

`x1 - x2 <= 0`

Solves both problems and prints the results.

***Task 2 (Feasibility and Constraint Check):***

Defines a minimization problem with constraints:

`3*x1 − 2*x2 ≥ 6`

`3*𝑥1 + 𝑥2 ≥ 3`

Solves the problem and checks if the solution satisfies the first constraint.

***Task 3 (Profit Maximization):***

Defines a profit maximization problem involving batches of three product types.
Constraints limit the number of batches based on resource availability.
Maximizes the profit function `30*x1 + 40*x2 + 45*x3` and prints the optimal solution.

_____

`pr2` is solving a Linear Programming (LP) problem using the PuLP library for optimization and visualizing the feasible region of the problem with Matplotlib.

The LP problem is defined as a minimization problem with the objective function: `4*x1 − 5*x2 + 15`

The decision variables are `x1` and `x2`, both having lower bounds of 0 (i.e., they must be non-negative).

Constraints:

`5*x1 + 3*x2 ≥ 23`

`x1 + 5*x2 ≤ 31`

`3*x1 - x2 ≤ 13`

`x1 - 2*x2 ≤ 2`

The `prob.solve()` function is used to find the optimal values of `x1` and `x2` that minimize the objective function while satisfying the constraints. The optimal solution is printed out along with the status of the solution.

Visualization:
- The constraints are visualized as lines on a 2D plot.
- The feasible region, which is the area where all constraints are satisfied, is shaded.
- The point corresponding to the optimal solution (minimum of the objective function) is plotted as a red dot.

________

`pr3` solves a Transportation Problem using Linear Programming (LP) with the PuLP library. The goal is to minimize the total transportation cost while satisfying supply and demand constraints.

Problem Definition:

A 4x4 matrix representing the transportation cost from each source (A1 to A4) to each destination (B1 to B4).
- Supply: The amount of goods available at each source (A1 to A4).
- Demand: The amount of goods required at each destination (B1 to B4).
  
Model Setup:
- The LP problem is defined as a minimization problem (LpMinimize).
- The decision variables are represented by route_vars[source, dest], which denotes the number of resources transported from source to dest. The variables are constrained to be non-negative integers.

The objective function is the total cost, which is calculated as the sum of the product of the transportation quantity and its respective cost.

Constraints:

- Supply Constraints: The sum of the resources sent from each source to all destinations must equal the supply at that source.
- Demand Constraints: The sum of the resources received at each destination from all sources must equal the demand at that destination.

The model is solved using model.solve(). The total cost is printed, followed by the quantity of resources transported from each source to each destination, along with the corresponding trip cost.
