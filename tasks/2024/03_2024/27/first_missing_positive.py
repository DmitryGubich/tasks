def first_missing_positive(nums: list[int]) -> int:
    i = 1
    for num in sorted(set(nums)):
        if num == i:
            i += 1
        elif num > 0:
            return i

    return i


if __name__ == "__main__":
    assert first_missing_positive(nums=[1, 2, 0]) == 3
    assert first_missing_positive(nums=[3, 4, -1, 1]) == 2
    assert first_missing_positive(nums=[7, 8, 9, 11, 12]) == 1
    assert first_missing_positive(nums=[1, 2]) == 3
