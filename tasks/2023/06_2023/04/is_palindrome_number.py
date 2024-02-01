def is_palindrome_number(x: int) -> bool:
    x = str(x)
    return x == x[::-1]


if __name__ == "__main__":
    assert is_palindrome_number(x=121) is True
    assert is_palindrome_number(x=-1121) is False
