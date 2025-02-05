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
