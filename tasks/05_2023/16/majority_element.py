from typing import List


def majority_element(nums: List[int]) -> int:
    sol = None
    cnt = 0
    for i in nums:
        if cnt == 0:
            sol = i
        cnt += 1 if i == sol else -1
    return sol


if __name__ == "__main__":
    assert 3 == majority_element(nums=[3, 2, 3])
    assert 2 == majority_element(nums=[2, 2, 1, 1, 1, 2, 2])
