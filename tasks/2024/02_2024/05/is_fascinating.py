def is_fascinating(n: int) -> bool:
    s = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    number = f"{n}{n * 2}{n * 3}"
    return sorted(number) == s and len(number) == 9


if __name__ == "__main__":
    assert is_fascinating(n=192) is True
    assert is_fascinating(n=100) is False
    assert is_fascinating(n=783) is False
