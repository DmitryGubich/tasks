def combine(n: int, k: int) -> list[list[int]]:
    def back_tracking(n: int, k: int, start: int, current: list[int]):
        if len(current) == k:
            result.append(list(current))
            return
        if len(current) + n - start < k:
            return
        for i in range(start + 1, n + 1):
            current.append(i)
            back_tracking(n, k, i, current)
            current.pop()

    result = []
    back_tracking(n, k, 0, [])
    return result


if __name__ == "__main__":
    assert combine(n=4, k=2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert combine(n=1, k=1) == [[1]]
