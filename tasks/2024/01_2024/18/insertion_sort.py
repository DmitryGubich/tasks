def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


if __name__ == "__main__":
    assert insertion_sort(nums=[1, 6, 3, 5, 2, 4]) == [1, 2, 3, 4, 5, 6]
