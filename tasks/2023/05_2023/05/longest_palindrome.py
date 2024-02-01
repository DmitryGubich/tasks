def longest_palindrome(s: str) -> str:
    longest = ""
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            word = s[i:j]
            if word == word[::-1] and len(word) > len(longest):
                longest = word
    return longest or s


if __name__ == "__main__":
    assert longest_palindrome(s="bb") == "bb"
    assert longest_palindrome(s="babad") == "bab"
    assert longest_palindrome(s="cbbd") == "bb"
