def remove_trailing_zeros(num: str) -> str:
    while num[-1] == "0":
        num = num[:-1]
    return num


if __name__ == "__main__":
    assert "512301" == remove_trailing_zeros(num="51230100")
    assert "123" == remove_trailing_zeros(num="123")
