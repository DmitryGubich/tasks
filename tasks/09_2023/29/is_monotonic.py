def is_monotonic(nums: list[int]) -> bool:
    if len(nums) < 2:
        return True
    direction = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            if direction == 0:
                direction = 1
            elif direction == -1:
                return False
        elif nums[i] < nums[i - 1]:
            if direction == 0:
                direction = -1
            elif direction == 1:
                return False

    return True


if __name__ == "__main__":
    assert is_monotonic(nums=[1, 2, 2, 3]) is True
    assert is_monotonic(nums=[6, 5, 4, 4]) is True
    assert is_monotonic(nums=[1, 3, 2]) is False
