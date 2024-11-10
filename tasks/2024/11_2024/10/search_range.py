def search_range(nums: list[int], target: int) -> list[int]:
    def search(elem: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] < elem:
                low = mid + 1
            else:
                high = mid
        return low

    lo = search(target)
    hi = search(target + 1) - 1

    if lo <= hi:
        return [lo, hi]

    return [-1, -1]

    # first, last = -1, -1
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         if first == -1:
    #             first = i
    #         last = i
    # return [first, last]


if __name__ == "__main__":
    assert search_range(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert search_range(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
