def find_max_average(nums: list[int], k: int) -> float:
    cur_sum = max_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        cur_sum = cur_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, cur_sum)
    return max_sum / k


if __name__ == "__main__":
    assert find_max_average(nums=[1, 12, -5, -6, 50, 3], k=4) == 12.75000
    assert find_max_average(nums=[5], k=1) == 5.0000
