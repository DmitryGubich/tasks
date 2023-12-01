def move_zeros(nums: list[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1


if __name__ == "__main__":
    numbers = [0, 1, 0, 3, 12]
    move_zeros(nums=numbers)
    assert numbers == [1, 3, 12, 0, 0]
