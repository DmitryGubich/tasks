def max_score(s: str) -> int:
    ones = s.count("1")
    zeros = 0
    ans = 0

    for i in range(len(s) - 1):
        if s[i] == "1":
            ones -= 1
        else:
            zeros += 1

        ans = max(ans, zeros + ones)

    return ans


if __name__ == "__main__":
    assert max_score(s="011101") == 5
    assert max_score(s="00111") == 5
    assert max_score(s="1111") == 3
    assert max_score(s="0000") == 3
