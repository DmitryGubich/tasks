def find_all_duplicates(nums: list[int]) -> list[int]:
    result = []
    seen = set()
    for num in nums:
        if num in seen:
            result.append(num)
        seen.add(num)

    return result


if __name__ == "__main__":
    assert find_all_duplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert find_all_duplicates(nums=[1, 1, 2]) == [1]
