from typing import List


def h_index(citations: List[int]) -> int:
    i = 0
    while i <= len([x for x in citations if x >= i]):
        i += 1
    return i - 1


if __name__ == "__main__":
    assert 3 == h_index(citations=[3, 0, 6, 1, 5])
    assert 1 == h_index(citations=[1, 3, 1])
    assert 0 == h_index(citations=[0])
    assert 1 == h_index(citations=[1])
    assert 2 == h_index(citations=[5, 4])
    assert 1 == h_index(citations=[5])
