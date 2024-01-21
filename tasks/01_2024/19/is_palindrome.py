def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    assert is_palindrome(s="aba") is True
    assert is_palindrome(s="abca") is False
    assert is_palindrome(s="racecar") is True
    assert is_palindrome(s="cbbcc") is False
