def dfs(grid, x, y, steps_left, visited):
    if steps_left < 0:
        return 0  # Out of steps
    if grid[x][y] == "C":
        return 1  # Reached a camp

    visited[x][y] = True
    count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(grid, new_x, new_y, visited):
            count += dfs(grid, new_x, new_y, steps_left - 1, visited)

    visited[x][y] = False  # Backtrack
    return count


def is_valid(grid, x, y, visited):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] != "X"


def find_possible_paths(grid, robot_location, max_steps):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    return dfs(grid, robot_location[0], robot_location[1], max_steps, visited)


if __name__ == "__main__":
    grid = [
        ["C", "X", "0", "0", "0", "0", "X", "C"],
        ["0", "X", "0", "0", "0", "0", "X", "X"],
        ["0", "X", "S", "C", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "X"],
    ]
    robot_location = (2, 2)
    max_steps = 9

    assert (
        find_possible_paths(
            grid=grid, robot_location=robot_location, max_steps=max_steps
        )
        == 63
    )
