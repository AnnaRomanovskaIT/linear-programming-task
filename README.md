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
