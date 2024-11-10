def search_range(nums: list[int], target: int) -> list[int]:
    def find_first(nums, target):
        low, high = 0, len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def find_last(nums, target):
        low, high = 0, len(nums) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    return [find_first(nums, target), find_last(nums, target)]

    # first, last = -1, -1
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         if first == -1:
    #             first = i
    #         last = i
    # return [first, last]


if __name__ == "__main__":
    assert search_range(nums=[2, 2], target=2) == [0, 1]
    assert search_range(nums=[1], target=1) == [0, 0]
    assert search_range(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert search_range(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
