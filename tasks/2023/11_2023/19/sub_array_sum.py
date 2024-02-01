def sub_array_sum(nums: list, k) -> int:
    result = 0
    sub_sum = 0
    prefix_sum_count = {0: 1}

    for i in range(len(nums)):
        sub_sum += nums[i]
        to_remove = sub_sum - k
        result += prefix_sum_count.get(to_remove, 0)
        prefix_sum_count[sub_sum] = prefix_sum_count.get(sub_sum, 0) + 1

    return result


if __name__ == "__main__":
    assert sub_array_sum(nums=[4, 2, 2, 1, 2, -3, 5, -8], k=5) == 5
