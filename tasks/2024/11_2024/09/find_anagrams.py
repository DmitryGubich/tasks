def find_anagrams(s: str, p: str) -> list[int]:
    # anagram is longer than word
    if len(p) > len(s):
        return []
    # init hashmaps for word and anagram for the first len(p) symbols
    s_count = {}
    p_count = {}
    for i in range(len(p)):
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        p_count[p[i]] = p_count.get(p[i], 0) + 1
    # check if we already have match
    result = [0] if s_count == p_count else []
    left = 0
    right = len(p)
    while right < len(s):
        s_count[s[right]] = s_count.get(s[right], 0) + 1
        s_count[s[left]] -= 1
        if s_count[s[left]] == 0:
            s_count.pop(s[left])
        left += 1
        right += 1
        if s_count == p_count:
            result.append(left)
    return result


if __name__ == "__main__":
    assert find_anagrams(s="cbaebabacd", p="abc") == [0, 6]
    assert find_anagrams(s="abab", p="ab") == [0, 1, 2]
