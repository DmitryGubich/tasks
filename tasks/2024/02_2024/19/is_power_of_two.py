def is_power_of_two_rec(n: int) -> bool:
    if n <= 0:
        return False
    elif n == 1:
        return True
    return n % 2 == 0 and is_power_of_two_rec(n // 2)


def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n / 2
    return True


if __name__ == "__main__":
    assert is_power_of_two(n=16) is True
    assert is_power_of_two(n=15) is False
