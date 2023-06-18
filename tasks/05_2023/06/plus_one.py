from typing import List


def plus_one(digits: List[int]) -> List[int]:
    result = int("".join((str(x) for x in digits))) + 1
    return [int(x) for x in str(result)]


if __name__ == "__main__":
    assert plus_one(digits=[1, 2, 3]) == [1, 2, 4]
    assert plus_one(digits=[4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one(digits=[9]) == [1, 0]
