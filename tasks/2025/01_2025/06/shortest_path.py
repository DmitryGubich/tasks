from collections import deque


def shortest_path(start: str, end: str) -> list[str]:
    graph = {}
    for edge in edges:
        a, b = edge.split(":")
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)

    if start not in graph or end not in graph:
        return []

    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        for neighbor in graph[node]:
            new_path = [*path, neighbor]
            queue.append(new_path)

    return []


if __name__ == "__main__":
    edges = [
        "s1:s2",
        "s1:s3",
        "s3:s5",
        "s2:s4",
        "s4:s5",
        "s1:s5",
    ]

    start = "s1"
    end = "s4"
    assert shortest_path(start=start, end=end) == ["s1", "s2", "s4"]
