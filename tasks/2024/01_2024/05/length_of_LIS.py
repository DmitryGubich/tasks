def length_of_lis(nums: list[int]) -> int:
    length = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            length += 1
    return length


if __name__ == "__main__":
    assert length_of_lis(nums=[10, 9, 2, 3, 5, 7, 101, 18]) == 4
    assert length_of_lis(nums=[0, 1, 0, 1, 2, 3]) == 4
    assert length_of_lis(nums=[4, 6, 5, 7, 9]) == 3
    assert length_of_lis(nums=[7, 7, 7, 7, 7, 7]) == 0
