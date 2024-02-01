def find_132_pattern(nums: list[int]) -> bool:
    if len(set(nums)) < 3:
        return False
    min_nums = [nums[0]]
    for i in range(1, len(nums)):
        min_nums.append(min(nums[i], min_nums[-1]))
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > min_nums[i]:
            while stack and stack[-1] <= min_nums[i]:
                stack.pop()
            if stack and min_nums[i] < stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
    return False


if __name__ == "__main__":
    assert find_132_pattern(nums=[1, 2, 3, 4]) is False
    assert find_132_pattern(nums=[3, 1, 4, 2]) is True
    assert find_132_pattern(nums=[-1, 3, 2, 0]) is True
    assert find_132_pattern(nums=[3, 5, 0, 3, 4]) is True
