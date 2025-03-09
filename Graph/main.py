class Graph:
    def __init__(self) -> None:
        self.adj_list: dict = {}

    def print_graph(self) -> None:
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex: str) -> bool:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1: str, v2: str) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1: str, v2: str) -> bool:
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex: str) -> bool:
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")
    my_graph.add_vertex("E")
    my_graph.add_edge("A", "B")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("C", "D")
    my_graph.add_edge("D", "E")
    my_graph.add_edge("E", "A")
    my_graph.print_graph()
    print("--" * 12)
    my_graph.remove_vertex("A")
    my_graph.print_graph()
