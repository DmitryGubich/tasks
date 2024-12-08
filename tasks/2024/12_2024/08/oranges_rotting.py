from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    fresh = 0
    rotten = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    result = 0

    while rotten and fresh > 0:
        result += 1
        for _ in range(len(rotten)):
            x, y = rotten.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xx, yy = x + dx, y + dy
                if xx < 0 or xx == rows or yy < 0 or yy == cols:
                    continue
                if grid[xx][yy] == 1:
                    fresh -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))

    return result if fresh == 0 else -1


if __name__ == "__main__":
    assert oranges_rotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
