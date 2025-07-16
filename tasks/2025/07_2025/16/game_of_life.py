def game_of_life(board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    0 = dead
    1 = alive
    To do in-place, we use temporary markers:
    - 2: was dead, now alive
    - -1: was alive, now dead
    """
    rows, cols = len(board), len(board[0])

    def count_live_neighbors(r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        live_neighbors = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc] == 1 or board[nr][nc] == -1:
                    live_neighbors += 1
        return live_neighbors

    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_live_neighbors(r, c)
            if board[r][c] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = -1  # alive -> dead
            elif live_neighbors == 3:
                board[r][c] = 2  # dead -> alive

    # Finalize board: replace temporary markers with final states
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1:
                board[r][c] = 0
            elif board[r][c] == 2:
                board[r][c] = 1


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    game_of_life(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
