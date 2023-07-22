adj_list = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": []
}
all_edges = {
    ("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")
}


class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

        if not self.is_directed:
            self.adj_list[v].append(u)

    def remove_edge(self, u, v):
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)

            if not self.is_directed:
                self.adj_list[v].remove(u)

    def add_vertex(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.adj_list[node] = []

    def remove_vertex(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            del self.adj_list[node]

            for n in self.adj_list:
                if node in self.adj_list[n]:
                    self.adj_list[n].remove(node)

    def degree(self, node):
        deg = len(self.adj_list[node])
        return deg

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->", self.adj_list[node])

    def get_neighbors(self, node):
        return self.adj_list[node]

    def has_edge(self, u, v):
        return v in self.adj_list[u]


nodes = ["A", "B", "C", "D", "E"]
graph = Graph(nodes, is_directed=True)
for u, v in all_edges:
    graph.add_edge(u, v)
graph.print_adj_list()
print("Degree of C: ", graph.degree("C"))
