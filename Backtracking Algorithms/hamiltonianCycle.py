def is_valid(v, pos, path, graph):
    # Check if the vertex v can be added to the path at position pos
    if v not in graph[path[pos - 1]]:
        return False

    if v in path:
        return False

    return True


def hamiltonian_cycle_util(graph, path, pos):
    num_vertices = len(graph)
    if pos == num_vertices:
        # Base case: All vertices are included in the path
        if path[pos - 1] in graph[path[0]]:
            # Check if the last vertex is connected to the starting vertex to form a cycle
            return True
        return False

    for v in range(1, num_vertices):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False


def hamiltonian_cycle(graph):
    num_vertices = len(graph)
    path = [-1] * num_vertices

    # Start with the first vertex as the starting point
    path[0] = 0

    if hamiltonian_cycle_util(graph, path, 1):
        return path
    return None


# Example usage
graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}

ham_cycle = hamiltonian_cycle(graph)
if ham_cycle is not None:
    print("Hamiltonian Cycle:")
    print(ham_cycle)
else:
    print("No Hamiltonian cycle found.")
