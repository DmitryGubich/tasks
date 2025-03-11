def num_jewels_in_stones(jewels: str, stones: str) -> int:
    jewels_set = set(jewels)
    counter = 0

    for stone in stones:
        if stone in jewels_set:
            counter += 1

    return counter


if __name__ == "__main__":
    assert num_jewels_in_stones(jewels="aA", stones="aAAbbbb") == 3
    assert num_jewels_in_stones(jewels="z", stones="ZZ") == 0
