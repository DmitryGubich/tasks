from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_better(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        hashmap[num] = i

    for i, num in enumerate(nums):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


def two_sum_best(nums: list[int], target: int) -> bool:
    hashset = set()

    for value in nums:
        complement = target - value
        if complement in hashset:
            return True
        hashset.add(value)

    return False


if __name__ == "__main__":
    assert two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum(nums=[3, 2, 4], target=6) == [1, 2]
    assert two_sum(nums=[3, 3], target=6) == [0, 1]
    assert two_sum(nums=[3, 1, 3], target=6) == [0, 2]

    assert two_sum_better(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum_better(nums=[3, 2, 4], target=6) == [1, 2]
    assert two_sum_better(nums=[3, 3], target=6) == [0, 1]
    assert two_sum_better(nums=[3, 1, 3], target=6) == [0, 2]

    assert two_sum_best(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum_best(nums=[3, 2, 4], target=6) == [1, 2]
    assert two_sum_best(nums=[3, 3], target=6) == [0, 1]
    assert two_sum_best(nums=[3, 1, 3], target=6) == [0, 2]
