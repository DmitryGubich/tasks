def is_palindrome(s: str) -> bool:
    s = [i for i in s.lower() if i.isalnum()]
    return s == s[::-1]


if __name__ == "__main__":
    assert is_palindrome(s="A man, a plan, a canal: Panama") is True
