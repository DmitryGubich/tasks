from typing import List


def majority_element(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


if __name__ == "__main__":
    assert majority_element(nums=[3, 2, 3]) == 3
    assert majority_element(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
