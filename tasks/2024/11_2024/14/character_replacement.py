def character_replacement(s: str, k: int) -> int:
    result, left, hash_map = 0, 0, {}
    for right in range(len(s)):
        hash_map[s[right]] = 1 + hash_map.get(s[right], 0)
        while (right - left + 1) - max(hash_map.values()) > k:
            hash_map[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    assert character_replacement(s="ABAB", k=2) == 4
    assert character_replacement(s="AABABBA", k=1) == 4
