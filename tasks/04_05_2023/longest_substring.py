def longest_substring(s: str) -> int:
    test = ""
    max_length = -1

    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    for i in list(s):
        if i in test:
            test = test[test.index(i) + 1:]
        test = test + i
        max_length = max(len(test), max_length)
    return max_length


if __name__ == '__main__':
    assert 3 == longest_substring(s="abcabcbb")  # The answer is "abc", with the length of 3.
    assert 1 == longest_substring(s="bbbbb")  # The answer is "b", with the length of 1.
    assert 3 == longest_substring(s="pwwkew")  # The answer is "wke", with the length of 3.
    assert 3 == longest_substring(s="dvdf")  # The answer is "wke", with the length of 3.
