def destination_city(paths: list[list[str]]) -> str:
    starts = set()
    finishes = set()

    for path in paths:
        starts.add(path[0])
        finishes.add(path[1])

    return next(iter(finishes - starts))


if __name__ == "__main__":
    assert (
        destination_city([["London", "Moscow"], ["Moscow", "Lima"], ["Lima", "Rome"]])
        == "Rome"
    )
    assert destination_city([["B", "C"], ["D", "B"], ["C", "A"]]) == "A"
