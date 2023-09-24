def subscriptions(subs: list[int]) -> int:
    plus_subs = subs[::2]
    minus_subs = subs[1::2]
    if len(subs) > 2:
        return sum(plus_subs) - sum(minus_subs) + max(minus_subs) - min(plus_subs)
    else:
        return abs(sum(plus_subs) - sum(minus_subs))


if __name__ == "__main__":
    assert subscriptions(subs=[1, 2]) == 1
    assert subscriptions(subs=[2, 2, 2]) == 2
    assert subscriptions(subs=[3, 5, 6, 8]) == 1
