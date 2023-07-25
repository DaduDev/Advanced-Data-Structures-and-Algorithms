class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph, add edges in both directions

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {', '.join(str(neighbor) for neighbor in self.graph[vertex])}")

# Example usage
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 1)

graph.display()
