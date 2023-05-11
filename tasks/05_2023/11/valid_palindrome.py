def valid_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    for i in range(len(s)):
        letters = list(s)
        del letters[i]
        if letters == letters[::-1]:
            return True
    return False


if __name__ == "__main__":
    assert valid_palindrome(s="aba") is True
    assert valid_palindrome(s="abca") is True
    assert valid_palindrome(s="cbbcc") is True
