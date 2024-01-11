class MyGraph:
    def __init__(self):
        self.adjacent_map = {}

    def add_node(self, node):
        self.adjacent_map[node] = []

    def add_edge(self, node1, node2):
        self.adjacent_map[node1].append(node2)
        self.adjacent_map[node2].append(node1)

    def show_connections(self):
        result = []
        for node in self.adjacent_map:
            result.append(f"{node} --> {', '.join(self.adjacent_map[node])}")
        print("\n".join(result))


if __name__ == "__main__":
    graph = MyGraph()
    graph.add_node("1")
    graph.add_node("2")
    graph.add_node("3")
    graph.add_node("4")

    graph.add_edge("1", "2")
    graph.add_edge("1", "3")
    graph.add_edge("2", "4")
    graph.add_edge("3", "2")
    graph.add_edge("4", "3")

    graph.show_connections()
