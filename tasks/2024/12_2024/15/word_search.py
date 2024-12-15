def exist(board: list[list[str]], word: str) -> bool:
    def back_tracking(i, j, ind):
        if ind == len(word):
            return True
        if (
            i < 0
            or i >= row
            or j < 0
            or j >= col
            or visited[i][j]
            or board[i][j] != word[ind]
        ):
            return False
        visited[i][j] = True
        if (
            back_tracking(i + 1, j, ind + 1)
            or back_tracking(i - 1, j, ind + 1)
            or back_tracking(i, j + 1, ind + 1)
            or back_tracking(i, j - 1, ind + 1)
        ):
            return True
        visited[i][j] = False
        return False

    row, col = len(board), len(board[0])
    visited = [[False] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if back_tracking(i, j, 0):
                return True
    return False


if __name__ == "__main__":
    assert (
        exist(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            word="ABCCED",
        )
        is True
    )
    assert (
        exist(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            word="SEE",
        )
        is True
    )
    assert (
        exist(
            board=[
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            word="ABCB",
        )
        is False
    )
