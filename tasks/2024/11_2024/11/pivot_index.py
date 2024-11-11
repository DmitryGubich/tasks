def pivot_index(nums: list[int]) -> int:
    l_sum = 0
    r_sum = sum(nums)
    for i in range(len(nums)):
        if l_sum + nums[i] == r_sum:
            return i
        else:
            l_sum += nums[i]
            r_sum -= nums[i]
    return -1


if __name__ == "__main__":
    assert pivot_index(nums=[1, 7, 3, 6, 5, 6]) == 3
