def score_of_string(s: str) -> int:
    score = 0
    for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))
    return score


if __name__ == "__main__":
    assert score_of_string(s="hello") == 13
    assert score_of_string(s="zaz") == 50
