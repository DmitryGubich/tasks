def maximum_count_n(nums: list[int]) -> int:
    # O(n)
    pos = neg = 0
    for i in nums:
        if i > 0:
            pos += 1
        if i < 0:
            neg += 1

    return max(pos, neg)


def maximum_count(nums: list[int]) -> int:
    # O(logN)
    def low():
        start, end = 0, len(nums) - 1
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid
        return index

    def high():
        start, end = 0, len(nums) - 1
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= 0:
                start = mid + 1
            else:
                end = mid - 1
                index = mid
        return index

    pos, neg = len(nums) - high(), low()
    return max(pos, neg)


if __name__ == "__main__":
    assert maximum_count(nums=[-2, -1, -1, 1, 2, 3]) == 3
    assert maximum_count(nums=[5, 20, 66, 1314]) == 4
