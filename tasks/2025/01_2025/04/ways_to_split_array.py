def ways_to_split_array(nums: list[int]) -> int:
    n = len(nums)
    result = 0
    pref_sum = [0] * n
    pref_sum[0] = nums[0]

    for i in range(1, n):
        pref_sum[i] = pref_sum[i - 1] + nums[i]

    for i in range(n - 1):
        left_sum = pref_sum[i]
        right_sum = pref_sum[n - 1] - pref_sum[i]

        if left_sum >= right_sum:
            result += 1

    return result


if __name__ == "__main__":
    assert ways_to_split_array(nums=[10, 4, -8, 7]) == 2
    assert ways_to_split_array(nums=[2, 3, 1, 0]) == 2
