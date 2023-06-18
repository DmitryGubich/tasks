from typing import List


def diagonal_sum(mat: List[List[int]]) -> int:
    result = 0
    first = 0
    last = len(mat) - 1
    for row in mat:
        result += row[first] if first == last else row[first] + row[last]
        first += 1
        last -= 1
    return result


if __name__ == "__main__":
    assert (
        diagonal_sum(
            mat=[
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
        )
        == 25
    )
    assert (
        diagonal_sum(
            mat=[
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
            ]
        )
        == 8
    )
    assert diagonal_sum(mat=[[5]]) == 5
