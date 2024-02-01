def set_mismatch(nums: list[int]) -> list[int]:
    n, a, b = len(nums), sum(nums), sum(set(nums))

    s = n * (n + 1) // 2

    return [a - b, s - b]


if __name__ == "__main__":
    assert set_mismatch(nums=[1, 2, 2, 4]) == [2, 3]
