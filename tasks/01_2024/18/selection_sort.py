def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        min_elem = i
        temp = nums[i]

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_elem]:
                min_elem = j

        nums[i] = nums[min_elem]
        nums[min_elem] = temp
    return nums


if __name__ == "__main__":
    assert selection_sort(nums=[1, 6, 3, 5, 2, 4]) == [1, 2, 3, 4, 5, 6]
