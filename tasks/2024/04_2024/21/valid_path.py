import collections


def valid_path(edges: list[list[int]], source: int, destination: int) -> bool:
    graph = collections.defaultdict(list)  # adjacent_map
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, visited):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, visited):
                    return True
        return False

    return dfs(source, set())


if __name__ == "__main__":
    assert valid_path(edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2) is True
    assert (
        valid_path(edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5) is False
    )
