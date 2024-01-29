def rob(nums: list[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]


if __name__ == "__main__":
    assert rob(nums=[1, 2, 3, 1]) == 4
    assert rob(nums=[2, 7, 9, 3, 1]) == 12
