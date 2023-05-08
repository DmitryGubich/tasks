from typing import List


def check_x_matrix(grid: List[List[int]]) -> bool:
    diagonals = []
    first = 0
    last = len(grid) - 1
    for row in grid:
        if first == last:
            diagonals.append(row[first])
        else:
            diagonals.append(row[first])
            diagonals.append(row[last])
        first += 1
        last -= 1

    flat_grid = [item for row in grid for item in row]
    for i in diagonals:
        if i in flat_grid:
            flat_grid.remove(i)

    return all(diagonals) and all(value == 0 for value in flat_grid)


if __name__ == "__main__":
    assert (
        check_x_matrix(
            grid=[
                [2, 0, 0, 1],
                [0, 3, 1, 0],
                [0, 5, 2, 0],
                [4, 0, 0, 2],
            ]
        )
        is True
    )
    assert (
        check_x_matrix(
            grid=[
                [5, 7, 0],
                [0, 3, 1],
                [0, 5, 0],
            ]
        )
        is False
    )
    assert (
        check_x_matrix(
            [
                [5, 0, 0, 1],
                [0, 4, 1, 5],
                [0, 5, 2, 0],
                [4, 1, 0, 2],
            ]
        )
        is False
    )
