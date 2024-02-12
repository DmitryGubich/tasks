from collections import defaultdict


def majority_element(nums: list[int]) -> int:
    hashmap = defaultdict(int)
    for i in nums:
        if hashmap.get(i, 0) == len(nums) // 2:
            return i
        hashmap[i] += 1


if __name__ == "__main__":
    assert majority_element(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element(nums=[3, 2, 3]) == 3
