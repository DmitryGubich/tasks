def find_best_sum(nums: list[int], k: int) -> int:
    return sum(sorted(nums)[-k:])


if __name__ == "__main__":
    assert find_best_sum(nums=[3, -1, 4, 12, -8, 5, 6], k=3) == 23
    assert find_best_sum(nums=[3, -1, 4, 12, -8, 5, 6], k=1) == 12
    assert find_best_sum(nums=[3, -1, 4, 12, -8, 5, 6], k=2) == 18
