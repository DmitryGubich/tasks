def find_duplicate(nums: list[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


if __name__ == "__main__":
    assert find_duplicate(nums=[1, 3, 4, 2, 2]) == 2
    assert find_duplicate(nums=[3, 1, 3, 4, 2]) == 3
