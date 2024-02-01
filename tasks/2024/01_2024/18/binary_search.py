def binary_search(nums: list[int], elem: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < elem:
            low = mid + 1
        elif nums[mid] > elem:
            high = mid - 1
        else:
            return mid

    return -1


if __name__ == "__main__":
    assert binary_search(nums=[1, 4, 6, 9, 12, 45, 76], elem=4) == 1
    assert binary_search(nums=[1, 4, 6, 9, 12, 45, 76], elem=93) == -1
