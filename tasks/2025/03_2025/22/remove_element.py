def remove_element(nums: list[int], val: int) -> int:
    l = 0
    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return l


if __name__ == "__main__":
    assert remove_element(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2) == 5
    assert remove_element(nums=[3, 2, 2, 3], val=3) == 2
