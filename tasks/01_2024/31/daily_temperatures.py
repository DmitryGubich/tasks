def daily_temperatures(temperatures: list[int]) -> list[int]:
    result = [0] * (len(temperatures))
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)

    return result


if __name__ == "__main__":
    assert daily_temperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
    assert daily_temperatures(temperatures=[30, 40, 50, 60]) == [1, 1, 1, 0]
