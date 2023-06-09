from typing import List


def last_stone_weight(stones: List[int]) -> int:
    while True:
        if len(stones) == 1:
            return stones[0]
        stones = sorted(stones, reverse=True)
        stones.append(stones.pop(0) - stones.pop(0))


if __name__ == "__main__":
    assert last_stone_weight(stones=[2, 7, 4, 1, 8, 1]) == 1
    assert last_stone_weight(stones=[1]) == 1
    assert last_stone_weight(stones=[1, 3]) == 2
