def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]


if __name__ == "__main__":
    assert k_closest(points=[[1, 3], [-2, 2]], k=1) == [[-2, 2]]
    assert k_closest(points=[[3, 3], [5, -1], [-2, 4]], k=2) == [[3, 3], [-2, 4]]
