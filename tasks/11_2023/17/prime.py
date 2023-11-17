def is_prime_number(n: int) -> bool:
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


if __name__ == "__main__":
    assert is_prime_number(n=49) is False
    assert is_prime_number(n=47) is True
