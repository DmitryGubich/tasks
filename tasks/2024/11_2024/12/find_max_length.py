def find_max_length(nums: list[int]) -> int:
    count_map = {}
    result = 0
    count = 0
    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1
        if count in count_map:
            result = max(result, i - count_map[count])
        else:
            count_map[count] = i

    return result


if __name__ == "__main__":
    assert find_max_length(nums=[0, 1]) == 2
    assert find_max_length(nums=[0, 1, 0]) == 2
