from typing import List


def sort_list(nums: List[int]) -> List[int]:
    # quick sort
    # less = []
    # equal = []
    # greater = []
    #
    # if len(nums) > 1:
    #     pivot = nums[0]
    #     for x in nums:
    #         if x < pivot:
    #             less.append(x)
    #         elif x == pivot:
    #             equal.append(x)
    #         else:
    #             greater.append(x)
    #     return sort_list(less) + equal + sort_list(greater)
    # else:
    #     return nums

    # count sort
    counts = {}
    min_v, max_v = min(nums), max(nums)
    for val in nums:
        counts[val] = counts.get(val, 0) + 1

    index = 0
    for val in range(min_v, max_v + 1):
        while counts.get(val, 0) > 0:
            nums[index] = val
            index += 1
            counts[val] -= 1
    return nums


if __name__ == "__main__":
    assert sort_list(nums=[5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert sort_list(nums=[5, 2, 3, 1]) == [1, 2, 3, 5]
