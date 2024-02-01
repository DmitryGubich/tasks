def fibonacci(num: int) -> int:
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
