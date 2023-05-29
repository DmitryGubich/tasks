from typing import List


def get_no_zero_integers(n: int) -> List[int]:
    for i in range(1, n):
        if "0" not in str(i) and "0" not in str(n - i):
            return [i, n - i]
    # for i in range(1, n + 1):
    #     for j in range(1, n + 1):
    #         if i + j == n and "0" not in str(i) and "0" not in str(j):
    #             return [i, j]


if __name__ == "__main__":
    assert [1, 1] == get_no_zero_integers(n=2)
    assert [2, 9] == get_no_zero_integers(n=11)
