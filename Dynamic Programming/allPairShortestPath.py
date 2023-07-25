INF = float('inf')

def all_pairs_shortest_path(graph):
    num_vertices = len(graph)
    dist = [[INF if i != j else 0 for j in range(num_vertices)] for i in range(num_vertices)]

    for u in range(num_vertices):
        for v, weight in graph[u].items():
            dist[u][v] = weight

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Example usage
graph = {
    0: {1: 3, 2: 6, 3: 15},
    1: {2: -2},
    2: {3: 2},
    3: {}
}

shortest_paths = all_pairs_shortest_path(graph)
for row in shortest_paths:
    print(row)
