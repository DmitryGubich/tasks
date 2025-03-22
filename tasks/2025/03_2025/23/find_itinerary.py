import collections


def find_itinerary(tickets: list[list[str]]) -> list[str]:
    graph = collections.defaultdict(list)
    for src, des in tickets:
        graph[src].append(des)

    for src in graph:
        graph[src].sort(reverse=True)

    stack = ["JFK"]
    res = []

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        else:
            res.append(stack.pop())

    return res[::-1]


if __name__ == "__main__":
    assert find_itinerary(
        tickets=[
            ["MUC", "LHR"],
            ["JFK", "MUC"],
            ["SFO", "SJC"],
            ["LHR", "SFO"],
        ]
    ) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    assert find_itinerary(
        tickets=[
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
    ) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
