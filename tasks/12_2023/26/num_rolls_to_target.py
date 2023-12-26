def num_rolls_to_target(target: int, dices: int = 2, sides: int = 6) -> int:
    def dp(cur, i):
        if i == 0:
            return 0
        elif i == 1 and 1 <= cur <= sides:
            return 1
        return sum(dp(cur - j, i - 1) for j in range(1, sides + 1))

    return dp(target, dices)


if __name__ == "__main__":
    assert num_rolls_to_target(target=3) == 2
    assert num_rolls_to_target(target=4) == 3
    assert num_rolls_to_target(target=7) == 6
