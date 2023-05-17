def climb_stairs(n: int) -> int:
    a, b = 0, 1
    for _ in range(0, n):
        c = a + b
        a, b = b, c
    return b


if __name__ == "__main__":
    assert 2 == climb_stairs(n=2)
    assert 3 == climb_stairs(n=3)
