def quick_sort(nums: list[int]) -> list[int]:
    less = []
    equal = []
    greater = []

    if nums:
        pivot = nums[0]
        for n in nums:
            if n > pivot:
                greater.append(n)
            elif n == pivot:
                equal.append(n)
            elif n < pivot:
                less.append(n)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return nums


if __name__ == "__main__":
    assert quick_sort(nums=[1, 6, 3, 5, 2, 4]) == [1, 2, 3, 4, 5, 6]
