from sys import maxsize


def min_sub_array_len(nums: list[int], target: int) -> int:
    result = maxsize
    left = total = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1

    return result if result != maxsize else 0


if __name__ == "__main__":
    assert min_sub_array_len(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
    assert min_sub_array_len(target=4, nums=[1, 4, 4]) == 1
