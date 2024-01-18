def bubble_sort(nums: list[int]) -> list[int]:
    for _ in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == "__main__":
    assert bubble_sort(nums=[1, 6, 3, 5, 2, 4]) == [1, 2, 3, 4, 5, 6]
