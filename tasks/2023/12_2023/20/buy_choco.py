def buy_choco(prices: list[int], money: int) -> int:
    first_min, second_min = float("inf"), float("inf")
    for price in prices:
        if price < first_min:
            first_min, second_min = price, first_min
        elif price < second_min:
            second_min = price
    leftover = money - first_min - second_min
    return leftover if leftover >= 0 else money


if __name__ == "__main__":
    assert buy_choco(prices=[98, 54, 6, 34, 66, 63, 52, 39], money=62) == 22
    assert buy_choco(prices=[69, 91, 78, 19, 40, 13], money=94) == 62
    assert buy_choco(prices=[3, 2, 3], money=3) == 3
