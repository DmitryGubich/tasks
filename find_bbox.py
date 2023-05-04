from typing import List


def find_bbox(coordinates: List[List[List[int]]]) -> List[List[int]]:
    max_x = min_x = coordinates[0][0][0]
    max_y = min_y = coordinates[0][0][1]
    for lt, rb in coordinates:
        min_x = min(lt[0], min_x)
        max_x = max(rb[0], max_x)
        max_y = max(lt[1], max_y)
        min_y = min(rb[1], min_y)

    return [[min_x, max_y], [max_x, min_y]]


if __name__ == "__main__":
    assert [[0, 20], [20, 0]] == find_bbox([[[10, 10], [20, 0]], [[0, 20], [20, 10]]])
