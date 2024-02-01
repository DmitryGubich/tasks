from typing import List


def h_index(citations: List[int]) -> int:
    i = 0
    while i <= len([x for x in citations if x >= i]):
        i += 1
    return i - 1


if __name__ == "__main__":
    assert h_index(citations=[3, 0, 6, 1, 5]) == 3
    assert h_index(citations=[1, 3, 1]) == 1
    assert h_index(citations=[0]) == 0
    assert h_index(citations=[1]) == 1
    assert h_index(citations=[5, 4]) == 2
    assert h_index(citations=[5]) == 1
