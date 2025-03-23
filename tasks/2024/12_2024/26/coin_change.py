# top to bottom solution

# def coin_change(coins: list[int], amount: int) -> int:
#     if amount == 0:
#         return 0
#     if amount < 0:
#         return -1
#     answer = maxsize
#     for coin in coins:
#         result = coin_change(coins, amount - coin)
#         if result != -1:
#             answer = min(answer, result + 1)
#     return answer if answer != maxsize else -1


# top to bottom solution with memoization

# def coin_change(coins: list[int], amount: int) -> int:
#     dp = [None] * (amount + 1)
#
#     def calculate(amount: int) -> int:
#         if amount == 0:
#             return 0
#         if amount < 0:
#             return -1
#         if dp[amount] is None:
#             answer = maxsize
#             for coin in coins:
#                 result = calculate(amount - coin)
#                 if result != -1:
#                     answer = min(answer, result + 1)
#             dp[amount] = answer if answer != maxsize else -1
#
#         return dp[amount]
#
#     return calculate(amount)


def coin_change(coins: list[int], amount: int) -> int:
    dp = [0] + [amount + 1] * amount

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == amount + 1 else dp[amount]


if __name__ == "__main__":
    assert coin_change(coins=[1, 2, 5], amount=11) == 3
    assert coin_change(coins=[2], amount=3) == -1
