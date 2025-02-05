from pulp import *
import math

costs = [[4, 5, 5, 7],
         [8, 7, 5, 4],
         [9, 6, 4, 5],
         [3, 2, 9, 3]]
supply = [100, 120, 150, 130]
demand = [140, 130, 90, 140]

model = LpProblem("Transportation_Problem", LpMinimize)

sources = ['A1', 'A2', 'A3', 'A4']
destinations = ['B1', 'B2', 'B3', 'B4']
routes = [(source, dest) for source in sources for dest in destinations]
route_vars = LpVariable.dicts("Route", routes, lowBound=0, cat='Integer')
model += lpSum(route_vars[source, dest] * costs[sources.index(source)][destinations.index(dest)]
               for source in sources for dest in destinations)

for source in sources:
    model += lpSum(route_vars[source, dest] for dest in destinations) == supply[sources.index(source)]
for dest in destinations:
    model += lpSum(route_vars[source, dest] for source in sources) == demand[destinations.index(dest)]
model.solve()

print("Total cost of all trips: =", value(model.objective))
for source, dest in routes:
    if route_vars[source, dest].varValue > 0:
        num_resources = route_vars[source, dest].varValue
        cost_per_resource = costs[sources.index(source)][destinations.index(dest)]
        trip_cost = num_resources * cost_per_resource
        print(f"Quantity of resources transported from {source} to {dest}: {num_resources}, Загальна вартість поїздки: {trip_cost}")
