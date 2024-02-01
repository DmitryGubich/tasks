def factorial(num: int) -> int:
    if num in (0, 1):
        return 1
    return num * factorial(num - 1)


def factorial_iter(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


if __name__ == "__main__":
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6
    assert factorial(2) == 2

    assert factorial_iter(5) == 120
    assert factorial_iter(4) == 24
    assert factorial_iter(3) == 6
    assert factorial_iter(2) == 2
