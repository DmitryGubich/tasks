def find_relative_ranks(score: list[int]) -> list[str]:
    score_map = {score[i]: i for i in range(len(score))}
    score.sort(reverse=True)
    result = [""] * len(score)
    for i in range(len(score)):
        if i == 0:
            result[score_map[score[i]]] = "Gold Medal"
        elif i == 1:
            result[score_map[score[i]]] = "Silver Medal"
        elif i == 2:
            result[score_map[score[i]]] = "Bronze Medal"
        else:
            result[score_map[score[i]]] = str(i + 1)

    return result


if __name__ == "__main__":
    assert find_relative_ranks(score=[5, 4, 3, 2, 1]) == [
        "Gold Medal",
        "Silver Medal",
        "Bronze Medal",
        "4",
        "5",
    ]
    assert find_relative_ranks(score=[10, 3, 8, 9, 4]) == [
        "Gold Medal",
        "5",
        "Bronze Medal",
        "Silver Medal",
        "4",
    ]
