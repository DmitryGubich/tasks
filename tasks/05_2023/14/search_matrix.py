from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    i = 0
    j = n - 1
    while True:
        try:
            element = matrix[i][j]
        except IndexError:
            return False

        if target == element:
            return True
        elif target < element:
            j -= 1
        else:
            i += 1


if __name__ == "__main__":
    assert (
        search_matrix(
            matrix=[
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            target=9,
        )
        is True
    )
    assert (
        search_matrix(
            matrix=[
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            target=20,
        )
        is False
    )
    assert search_matrix(matrix=[[-5]], target=-5) is True
