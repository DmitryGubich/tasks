from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    dp = [0] + [amount + 1] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] == amount + 1 else dp[amount]


if __name__ == "__main__":
    assert coin_change(coins=[1, 2, 5], amount=11) == 3
    assert coin_change(coins=[2], amount=3) == -1
