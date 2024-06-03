"""
Dijkestra's algorithm is used to find the shortest path between two nodes in a graph.
"""


import heapq


graph = {
    'A': [('C', 3), ('F', 2)],
    'B': [('D', 1), ('E', 2), ('G', 2)],
    'C': [('A', 3), ('D', 4), ('E', 1)],
    'D': [('B', 1), ('C', 4)],
    'E': [('B', 2), ('C', 1), ('F', 3)],
    'F': [('A', 2), ('E', 3), ('G', 5)],
    'G': [('B', 2), ('F', 5)]
}

def djikestra_shortest_path(graph, start, end):
    # Initialize the distance array
    costs = {node: float('infinity') for node in graph}
    costs[start] = 0

    # Initialize the priority queue
    pq = [(0, start)]

    while pq:
        # fetch priority queue
        current_cost, current_node = heapq.heappop(pq)

        # check cost
        if current_cost > costs[current_node]:
            continue

        # visit the neighbors
        for neighbor, weight in graph[current_node]:
            # new cost
            new_cost = current_cost + weight
            # If new cost is less than the current cost, update the cost and add the neighbor to the priority queue
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return costs[end]


print(djikestra_shortest_path(graph, 'A', 'B'))  # Output: 6
# print(djikestra_shortest_path(graph, 'A', 'G'))  # Output: 7


# def print_shortes_path(graph, src, dst):
#     distance = {node: float('infinity') for node in graph}
#     distance[src] = 0

#     pq = [(0, src)]
#     parent = {src: None}

#     while pq:
#         current_distance, current_node = heapq.heappop(pq)

#         if current_distance > distance[current_node]:
#             continue

#         for neighbor, weight in graph[current_node]:
#             new_distance = current_distance + weight

#             if new_distance < distance[neighbor]:
#                 distance[neighbor] = new_distance
#                 parent[neighbor] = current_node
#                 heapq.heappush(pq, (new_distance, neighbor))

#     path = []
#     while dst:
#         path.append(dst)
#         dst = parent[dst]

#     return path[::-1]

# print(print_shortes_path(graph, 'A', 'B'))  # Output: ['A', 'F', 'E', 'B']
    