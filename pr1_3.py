from pulp import *

def task1():
    prob_min = LpProblem("Minimization_Problem", LpMinimize)
    
    x1 = LpVariable("x1", lowBound=0.5, cat='Continuous')
    x2 = LpVariable("x2", upBound=4, cat='Continuous')
    
    prob_min += 2*x1 + 2*x2  # Objective function for minimization
    # Constraints
    prob_min += x1 + x2 >= 2
    prob_min += x1 + x2 <= 5
    prob_min += x1 - x2 <= 0
    
    prob_min.solve()
    
    print("Minimum value of the function:", value(prob_min.objective))

    prob_max = LpProblem("Maximization_Problem", LpMaximize)
    prob_max += 2*x1 + 2*x2  # Objective function for maximization
    # Constraints
    prob_max += x1 + x2 >= 2
    prob_max += x1 + x2 <= 5
    prob_max += x1 - x2 <= 0
    
    prob_max.solve()
    
    print("Maximum value of the function:", value(prob_max.objective))
    print()

def task2():
    prob = LpProblem("Min", LpMinimize)
    x1 = LpVariable("x1", upBound=3)
    x2 = LpVariable("x2", lowBound=0)

    # Constraints
    prob += 3*x1 - 2*x2 >= 6
    prob += 3*x1 + x2 >= 3

    prob.solve()
    print("Solution range from", value(x2), "to", value(x1))
    if value(3*x1 - 2*x2) >= 6:
        print("The solution satisfies the constraint 3*x1 - 2*x2 >= 6")
    else:
        print("The solution does NOT satisfy the constraint 3*x1 - 2*x2 >= 6")
    print()

def task3():
    prob = LpProblem("maxProfit", LpMaximize)
    
    x1 = LpVariable("Number of batches of the first type of products", lowBound=0, cat='Integer')
    x2 = LpVariable("Number of batches of the second type of products", lowBound=0, cat='Integer')
    x3 = LpVariable("Number of batches of the third type of products", lowBound=0, cat='Integer')
    
    # Constraints
    prob += 3*x1 + 2*x2 + 6*x3 <= 76 
    prob += 2*x1 + 5*x2 + 3*x3 <= 73 
    prob += 4*x1 + 3*x2 + 5*x3 <= 83 
    
    # Adding the objective function for maximization (Profit)
    prob += 30*x1 + 40*x2 + 45*x3

    # Solving the problem
    prob.solve()

    print("Optimal number of batches for the first type of products =", value(x1))
    print("Optimal number of batches for the second type of products =", value(x2))
    print("Optimal number of batches for the third type of products =", value(x3))
    print("Total revenue (in cents) =", value(prob.objective))

def main():
    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()
