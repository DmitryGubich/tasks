def find_peak_element(nums: list[int]) -> int:
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    assert find_peak_element(nums=[1, 2, 3, 1]) == 2
    assert find_peak_element(nums=[1, 2, 1, 3, 5, 6, 4]) == 5
