def is_safe(vertex, color, graph, color_assignment, num_colors):
    # Check if it is safe to assign 'color' to 'vertex'
    for neighbor in graph[vertex]:
        if color_assignment[neighbor] == color:
            return False
    return True


def graph_coloring_util(graph, num_colors, vertex, color_assignment):
    # Base case: All vertices are assigned colors
    if vertex == len(graph):
        return True

    for color in range(1, num_colors + 1):
        if is_safe(vertex, color, graph, color_assignment, num_colors):
            color_assignment[vertex] = color

            # Recursive call to assign colors to the remaining vertices
            if graph_coloring_util(graph, num_colors, vertex + 1, color_assignment):
                return True

            # Backtrack if the current assignment is not feasible
            color_assignment[vertex] = 0

    return False


def graph_coloring(graph, num_colors):
    num_vertices = len(graph)
    color_assignment = [0] * num_vertices

    if graph_coloring_util(graph, num_colors, 0, color_assignment):
        return color_assignment
    else:
        return None


# Example usage
# Representing the graph as an adjacency list
graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2]
}
num_colors = 3

color_assignment = graph_coloring(graph, num_colors)
if color_assignment is not None:
    print("Graph Coloring Solution:")
    for vertex, color in enumerate(color_assignment):
        print(f"Vertex {vertex}: Color {color}")
else:
    print("No valid graph coloring found.")
