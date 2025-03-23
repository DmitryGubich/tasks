def target_sum(nums: list[int], target: int) -> int:
    dp = {}

    def backtrack(i, total):
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total) in dp:
            return dp[(i, total)]

        dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])

        return dp[(i, total)]

    return backtrack(0, 0)


if __name__ == "__main__":
    assert target_sum(nums=[1, 1, 1, 1, 1], target=3) == 5
    assert target_sum(nums=[1], target=1) == 1
