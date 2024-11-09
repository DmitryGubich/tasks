def longest_substring(s: str) -> int:
    left = right = 0
    answer = set()
    max_length = 0

    while right < len(s):
        if s[right] not in answer:
            answer.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            while s[right] in answer:
                answer.remove(s[left])
                left += 1
    return max_length


if __name__ == "__main__":
    assert longest_substring(s="abcabcbb") == 3
    assert longest_substring(s="bbbbb") == 1
    assert longest_substring(s="pwwkew") == 3
    assert longest_substring(s="dvdf") == 3
