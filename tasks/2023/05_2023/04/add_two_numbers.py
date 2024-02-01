from typing import List


def add_two_numbers(l1: List, l2: List) -> List:
    a = int(("".join(str(x) for x in l1))[::-1])
    b = int(("".join(str(x) for x in l2))[::-1])
    return [int(i) for i in str(a + b)][::-1]


if __name__ == "__main__":
    assert add_two_numbers(l1=[2, 4, 3], l2=[5, 6, 4]) == [7, 0, 8]
    assert add_two_numbers(l1=[0], l2=[0]) == [0]
    assert add_two_numbers(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9]) == [
        8,
        9,
        9,
        9,
        0,
        0,
        0,
        1,
    ]
