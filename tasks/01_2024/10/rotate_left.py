def rotate_left(a: list, d: int) -> list:
    result = []
    for i in range(len(a)):
        result.append(a[(i + d) % len(a)])
    return result


if __name__ == "__main__":
    assert rotate_left(a=[1, 2, 3, 4, 5], d=4) == [5, 1, 2, 3, 4]
