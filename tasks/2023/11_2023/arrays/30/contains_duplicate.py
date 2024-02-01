def contains_duplicate(nums: list[int]) -> bool:
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


if __name__ == "__main__":
    assert contains_duplicate(nums=[1, 2, 3, 1]) is True
    assert contains_duplicate(nums=[1, 2, 3, 4]) is False
