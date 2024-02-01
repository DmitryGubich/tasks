def card_counter(n: int, k: int, cards: list[int]) -> int:
    if k >= n:
        return sum(cards)
    max_sum = -1
    sum_l = sum(cards[:0])
    sum_r = sum(cards[: -k - 1 : -1])
    cur_sum = sum_l + sum_r
    if cur_sum > max_sum:
        max_sum = cur_sum
    for i in range(0, k):
        sum_l += cards[i]
        sum_r -= cards[-k + i]
        cur_sum = sum_l + sum_r
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum


if __name__ == "__main__":
    assert card_counter(n=7, k=3, cards=[5, 8, 2, 1, 3, 4, 11]) == 24
    assert card_counter(n=7, k=4, cards=[1, 1, 9, 2, 2, 2, 6]) == 17
    assert card_counter(n=5, k=5, cards=[1, 2, 3, 4, 5]) == 15
