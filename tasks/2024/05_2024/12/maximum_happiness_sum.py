def maximum_happiness_sum(happiness: list[int], k: int) -> int:
    happiness.sort(reverse=True)
    result = 0

    for i in range(k):
        current = max(happiness[i] - i, 0)
        result += current

    return result


if __name__ == "__main__":
    assert maximum_happiness_sum(happiness=[1, 2, 3], k=2) == 4
    assert maximum_happiness_sum(happiness=[1, 1, 1, 1], k=2) == 1
