def remove_trailing_zeros(num: str) -> str:
    while num[-1] == "0":
        num = num[:-1]
    return num


if __name__ == "__main__":
    assert remove_trailing_zeros(num="51230100") == "512301"
    assert remove_trailing_zeros(num="123") == "123"
