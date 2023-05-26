from typing import List


def move_zeroes(nums: List[int]) -> List[int]:
    return [x for x in nums if x != 0] + [x for x in nums if x == 0]


if __name__ == "__main__":
    assert [1, 3, 12, 0, 0] == move_zeroes(nums=[0, 1, 0, 3, 12])
    assert [0] == move_zeroes(nums=[0])
