def max_vowels(s: str, k: int) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    max_number = 0
    for i in range(len(s)):
        number = 0
        part = s[i : i + k]
        for vowel in vowels:
            number += part.count(vowel)
        max_number = max(max_number, number)
    return max_number

    # count = 0
    # for i in range(k):
    #     count += int(s[i] in vowels)
    # max_num = count
    #
    # for end in range(k, len(s)):
    #     start = end - k + 1
    #     if s[start - 1] in vowels:
    #         count = count - 1
    #     if s[end] in vowels:
    #         count = count + 1
    #     max_num = max(max_num, count)
    # return max_num


if __name__ == "__main__":
    assert 3 == max_vowels(s="abciiidef", k=3)
    assert 2 == max_vowels(s="aeiou", k=2)
    assert 2 == max_vowels(s="leetcode", k=3)
    assert 0 == max_vowels(s="lkdf", k=3)
    assert 4 == max_vowels(s="weallloveyou", k=7)
