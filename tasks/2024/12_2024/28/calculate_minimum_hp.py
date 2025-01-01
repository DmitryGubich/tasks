from sys import maxsize


def calculate_minimum_hp(dungeon: list[list[int]]) -> int:
    if len(dungeon) == 0 or len(dungeon[0]) == 0:
        return 1

    dp = [[None] * (len(dungeon[0]) + 1) for _ in range(len(dungeon) + 1)]

    def helper(i: int, j: int) -> int:
        n, m = len(dungeon), len(dungeon[0])
        if i == n or i < 0 or j == m or j < 0:
            return maxsize
        if i == n - 1 and j == m - 1:
            return 1 - dungeon[i][j] if dungeon[i][j] <= 0 else 1
        if dp[i][j] is None:
            bot = helper(i=i + 1, j=j)
            right = helper(i=i, j=j + 1)
            way = min(bot, right)
            dp[i][j] = max(way - dungeon[i][j], 1)

        return dp[i][j]

    return helper(i=0, j=0)


if __name__ == "__main__":
    assert calculate_minimum_hp(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7
    assert calculate_minimum_hp(dungeon=[[0]]) == 1
