def kth_factor(n: int, k: int) -> int:
    result = [i for i in range(1, n + 1) if n % i == 0]
    return result[k - 1] if k <= len(result) else -1


if __name__ == "__main__":
    assert 3 == kth_factor(n=12, k=3)
    assert 7 == kth_factor(n=7, k=2)
    assert -1 == kth_factor(n=4, k=4)
