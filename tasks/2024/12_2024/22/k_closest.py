import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for x, y in points:
        distance = -(x**2 + y**2)
        heapq.heappush(heap, (distance, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    assert k_closest(points=[[1, 3], [-2, 2]], k=1) == [[-2, 2]]
    assert k_closest(points=[[3, 3], [5, -1], [-2, 4]], k=2) == [[-2, 4], [3, 3]]
