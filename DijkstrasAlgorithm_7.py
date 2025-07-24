import math

graph = {}
graph["начало"] = {}
graph["начало"]["a"] = 6
graph["начало"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["конец"] = 5
graph["конец"] = {}

infinty = math.inf
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinty

parents = {}
parents["a"] = "начало"
parents["b"] = "начало"
parents["fin"] = None

processed = set()


def find_lowest_cost_node(cost):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)

print(cost)
