def first_recurring_number(nums: list[int]) -> int | None:
    hashset = set()
    for i in nums:
        if i in hashset:
            return i
        hashset.add(i)
    return None


if __name__ == "__main__":
    assert first_recurring_number(nums=[1, 2, 3, 1]) == 1
    assert first_recurring_number(nums=[1, 2, 3, 4]) is None
