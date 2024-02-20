def missing_number(nums: list[int]) -> int:
    nums = set(nums)
    for i in range(len(nums) + 1):
        if i not in nums:
            return i


def missing_number_math(nums: list[int]) -> int:
    n = len(nums)
    math_sum = (n + 1) * n // 2
    act_sum = sum(nums)
    return math_sum - act_sum


if __name__ == "__main__":
    assert missing_number(nums=[3, 0, 1]) == 2
    assert missing_number(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
