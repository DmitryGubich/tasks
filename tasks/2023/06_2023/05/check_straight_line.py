from typing import List


def check_straight_line(coordinates: List[List[int]]) -> bool:
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
            return False

    return True


if __name__ == "__main__":
    assert check_straight_line(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) is True
    assert (
        check_straight_line(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]) is False
    )
