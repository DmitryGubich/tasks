from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    assert contains_duplicate(nums=[1, 2, 3, 1]) is True
    assert contains_duplicate(nums=[1, 2, 3, 4]) is False
