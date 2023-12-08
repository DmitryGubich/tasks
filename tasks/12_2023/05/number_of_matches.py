def number_of_matches(n: int | float) -> int:
    teams = int(n)

    if n == 1:
        return 0
    if n == 2:
        return 1

    matches = n / 2 if teams % 2 == 0 else (n - 1) / 2

    if teams % 2 == 0:
        matches += number_of_matches(n / 2)
    else:
        matches += number_of_matches((n - 1) / 2 + 1)

    return int(matches)


if __name__ == "__main__":
    assert number_of_matches(n=7) == 6
    assert number_of_matches(n=14) == 13
