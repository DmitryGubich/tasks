def move_zeroes(nums: list[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if (
            nums[i] != 0
        ):  # if we want to move zeros in the beginning, we need nums[i] == 0 clause
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


if __name__ == "__main__":
    # zeros at the end
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums=nums)
    assert nums == [1, 3, 12, 0, 0]
    # zeros in the beginning
    # nums = [0, 1, 0, 3, 12]
    # move_zeroes(nums=nums)
    # assert nums == [0, 0, 1, 3, 12]
