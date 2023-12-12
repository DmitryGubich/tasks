def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]

    return result


if __name__ == "__main__":
    assert transpose_matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
