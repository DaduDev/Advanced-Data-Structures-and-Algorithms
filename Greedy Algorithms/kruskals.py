def find_parent(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find_parent(parent, parent[vertex])
    return parent[vertex]

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((weight, u, v))

    edges.sort()  # Sort edges in ascending order of weights

    parent = {vertex: vertex for vertex in graph}
    minimum_spanning_tree = set()

    for weight, u, v in edges:
        parent_u = find_parent(parent, u)
        parent_v = find_parent(parent, v)

        if parent_u != parent_v:
            minimum_spanning_tree.add((u, v))
            parent[parent_u] = parent_v  # Union the sets by updating the parent

    return minimum_spanning_tree


# Example usage
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)