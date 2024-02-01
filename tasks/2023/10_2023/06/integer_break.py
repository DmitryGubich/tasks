def integer_break(n: int) -> int:
    if n <= 3:
        return n - 1
    if n % 3 == 0:
        return 3 ** (n // 3)
    if n % 3 == 1:
        return 3 ** (n // 3 - 1) * 4
    return 3 ** (n // 3) * 2


if __name__ == "__main__":
    assert integer_break(n=2) == 1
    assert integer_break(n=10) == 36
