def reverse_integer(x: int) -> int:
    rev = int(str(abs(x))[::-1])
    return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0


if __name__ == "__main__":
    assert 0 == reverse_integer(x=1563847412)
    assert -321 == reverse_integer(x=-123)
    assert 21 == reverse_integer(x=120)
