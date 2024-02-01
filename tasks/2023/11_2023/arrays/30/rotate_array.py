def rotate_array(nums: list[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(nums=nums, k=3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [1, 2, 3]
    rotate_array(nums=nums, k=5)
    assert nums == [2, 3, 1]
