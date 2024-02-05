def first_uniq_char(s: str) -> int:
    hashmap = {}
    for i in s:
        hashmap[i] = hashmap.get(i, 0) + 1

    for i, char in enumerate(s):
        if hashmap[char] == 1:
            return i
    return -1


if __name__ == "__main__":
    assert first_uniq_char(s="leetcode") == 0
    assert first_uniq_char(s="loveleetcode") == 2
