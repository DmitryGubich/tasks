def max_profit(prices: list[int]) -> int:
    min_price, profit = prices[0], 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = max(price - min_price, profit)

    return profit


if __name__ == "__main__":
    assert max_profit(prices=[7, 1, 5, 3, 6, 4]) == 5
    assert max_profit(prices=[7, 6, 4, 3, 1]) == 0
