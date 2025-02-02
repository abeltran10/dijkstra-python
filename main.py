def dijkstra(graph, start):
    shortest_distances = {node: 10000 for node in graph}
    shortest_distances[start] = 0

    for node, w in graph[start].items(): shortest_distances[node] = w

    added = {start}

    in_frontier_from = {node: start for node, w in graph[start].items()}

    previous_nodes = {node: None for node in graph}

    while len(in_frontier_from) > 0:
        # print(f"frontier: {in_frontier_from}")

        dmin, u, v = min((shortest_distances[v], u, v) for v, u in in_frontier_from.items())

        # print(f"min: {v}:{u}")

        del in_frontier_from[v]
        # print(f"frontier: {in_frontier_from}")

        added.add(v)
        # print(f"added: {added}")

        previous_nodes[v] = u
        # print(f"previus nodes: {previous_nodes}")

        for neighbor, weight in graph[v].items():
            # print(f"{neighbor}:{weight}")
            if neighbor not in added and shortest_distances[v] + weight < shortest_distances[neighbor]:
                shortest_distances[neighbor] = shortest_distances[v] + weight
                in_frontier_from[neighbor] = v

    return shortest_distances, previous_nodes


def reconstruct_path(previous_nodes, target):
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()

    return path



graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1, 'D': 3, 'E': 7},
    'C': {'A': 3, 'B': 1, 'E': 5},
    'D': {'B': 3, 'E': 2, 'F': 4},
    'E': {'B': 7, 'D': 2, 'F': 3},
    'F': {'D': 4, 'E': 3}
}

start_node = 'A'
end_node = 'F'

# Calcular las distancias más cortas y los caminos
shortest_distances, previous_nodes = dijkstra(graph, start_node)

# Mostrar la distancia más corta
print(f"Distancia más corta de {start_node} a {end_node}: {shortest_distances[end_node]}")

# Reconstruir y mostrar el camino más corto
path = reconstruct_path(previous_nodes, end_node)
print(f"Camino más corto de {start_node} a {end_node}: {path}")
