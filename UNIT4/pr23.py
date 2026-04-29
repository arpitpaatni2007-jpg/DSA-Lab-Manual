class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


g = Graph()

edges = [
    ('A', 'B', 2),
    ('A', 'C', 4),
    ('B', 'D', 1),
    ('C', 'D', 3),
    ('D', 'E', 5),
    ('E', 'A', 2)
]

for u, v, w in edges:
    g.add_edge(u, v, w)

print("Adjacency List:")
g.display()