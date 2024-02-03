def sequential_digits(low: int, high: int) -> list[int]:
    result = []
    superset = "123456789"

    for i in range(len(str(low)), len(str(high)) + 1):
        for j in range(0, 9 - i + 1):
            num = int(superset[j : j + i])
            if low <= num <= high:
                result.append(num)

    return result


if __name__ == "__main__":
    assert sequential_digits(low=100, high=300) == [123, 234]
    assert sequential_digits(low=1000, high=5000) == [1234, 2345, 3456, 4567]
