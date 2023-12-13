def num_special(matrix: list[list[int]]) -> int:
    result = 0
    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                continue

            flag = True

            for r in range(m):
                if r != row and matrix[r][col] == 1:
                    flag = False
                    break

            for c in range(n):
                if c != col and matrix[row][c] == 1:
                    flag = False
                    break

            if flag:
                result += 1

    return result


if __name__ == "__main__":
    assert num_special(matrix=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]) == 1
    assert num_special(matrix=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert (
        num_special(matrix=[[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
        == 2
    )
