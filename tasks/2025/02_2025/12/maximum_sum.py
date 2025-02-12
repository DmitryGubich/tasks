def maximum_sum(nums: list[int]) -> int:
    def get_sum(n: int) -> int:
        return sum(int(digit) for digit in str(n))

    result = -1
    groups = {}
    for num in nums:
        key = get_sum(num)
        if key in groups:
            result = max(result, num + groups[key])
            groups[key] = max(groups[key], num)
        else:
            groups[key] = num

    return result


if __name__ == "__main__":
    assert maximum_sum(nums=[18, 43, 36, 13, 7]) == 54
    assert maximum_sum(nums=[10, 12, 19, 14]) == -1
