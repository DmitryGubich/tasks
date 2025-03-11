from collections import Counter


def is_possible_to_split(nums: list[int]) -> bool:
    c = Counter(nums)
    for v in c.values():
        if v > 2:
            return False
    return True


if __name__ == "__main__":
    assert is_possible_to_split(nums=[1, 1, 2, 2, 3, 4]) is True
    assert is_possible_to_split(nums=[1, 1, 1, 1]) is False
