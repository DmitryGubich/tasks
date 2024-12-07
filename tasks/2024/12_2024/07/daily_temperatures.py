# key points:
# - moving from right to left
# - store monotonic stack
def daily_temperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * (len(temperatures))

    for i in range(len(temperatures) - 1, -1, -1):
        while stack and stack[-1][0] <= temperatures[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1][1] - i
        stack.append((temperatures[i], i))

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
