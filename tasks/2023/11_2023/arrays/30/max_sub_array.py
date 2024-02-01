def max_sub_array(nums: list[int]) -> int:
    max_sum = float("-inf")
    current_sum = 0

    for num in nums:
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum


if __name__ == "__main__":
    assert max_sub_array(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array(nums=[5, 4, -1, 7, 8]) == 23
