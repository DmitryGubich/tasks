def num_identical_pairs(nums: list[int]) -> int:
    repeat = {}
    result = 0
    for v in nums:
        if v in repeat:
            result += repeat[v]
            repeat[v] += 1
        else:
            repeat[v] = 1
    return result


if __name__ == "__main__":
    assert num_identical_pairs(nums=[1, 2, 3, 1, 1, 3]) == 4
    assert num_identical_pairs(nums=[1, 1, 1, 1]) == 6
