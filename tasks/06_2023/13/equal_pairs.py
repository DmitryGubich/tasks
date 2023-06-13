from typing import List


def equal_pairs(grid: List[List[int]]) -> int:
    result = 0
    columns = []
    for i in range(len(grid)):
        columns.append([grid[j][i] for j in range(len(grid))])

    for row in grid:
        result += columns.count(row)
    return result


if __name__ == "__main__":
    assert 1 == equal_pairs(
        grid=[
            [3, 2, 1],
            [1, 7, 6],
            [2, 7, 7],
        ]
    )
    assert 3 == equal_pairs(
        grid=[
            [3, 1, 2, 2],
            [1, 4, 4, 5],
            [2, 4, 2, 2],
            [2, 4, 2, 2],
        ]
    )
    assert 3 == equal_pairs(
        grid=[
            [3, 1, 2, 2],
            [1, 4, 4, 4],
            [2, 4, 2, 2],
            [2, 5, 2, 2],
        ]
    )
