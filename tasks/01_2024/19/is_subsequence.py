def is_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


if __name__ == "__main__":
    assert is_subsequence(s="abc", t="ahbgdc") is True
    assert is_subsequence(s="axc", t="ahbgdc") is False
