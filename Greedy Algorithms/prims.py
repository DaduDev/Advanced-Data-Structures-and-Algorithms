import heapq

def prim(graph):
    mst = set()
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [(cost, start_vertex, neighbor) for neighbor, cost in graph[start_vertex].items()]
    heapq.heapify(edges)

    while edges:
        cost, u, v = heapq.heappop(edges)
        if v not in visited:
            mst.add((u, v))
            visited.add(v)
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))

    return mst


# Example usage
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)