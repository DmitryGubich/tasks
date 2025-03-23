def num_islands(grid: list[list[str]]) -> int:
    def dfs(row: int, col: int, grid: list[list[str]]):
        if is_inbounds(grid, row, col):
            grid[row][col] = "0"
            for new_row, new_col in [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]:
                dfs(new_row, new_col, grid)

    def is_inbounds(grid: list[list[str]], row: int, col: int) -> bool:
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"

    count = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if grid[row][col] == "1":
                count += 1
                dfs(row, col, grid)

    return count


if __name__ == "__main__":
    assert (
        num_islands(
            grid=[
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        num_islands(
            grid=[
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
