from typing import List


def can_make_arithmetic_progression(arr: List[int]) -> bool:
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return False
    return True


if __name__ == "__main__":
    assert can_make_arithmetic_progression(arr=[3, 5, 1]) is True
    assert can_make_arithmetic_progression(arr=[1, 2, 4]) is False
