def kth_factor(n: int, k: int) -> int:
    result = [i for i in range(1, n + 1) if n % i == 0]
    return result[k - 1] if k <= len(result) else -1


if __name__ == "__main__":
    assert kth_factor(n=12, k=3) == 3
    assert kth_factor(n=7, k=2) == 7
    assert kth_factor(n=4, k=4) == -1
