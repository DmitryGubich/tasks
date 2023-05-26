def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    assert is_anagram(s="anagram", t="nagaram") is True
    assert is_anagram(s="rat", t="car") is False
