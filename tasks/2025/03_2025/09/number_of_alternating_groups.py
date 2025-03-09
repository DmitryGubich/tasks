def number_of_alternating_groups(colors: list[int]) -> int:
    n = len(colors)
    result = 0
    colors += colors

    for i in range(n):
        if colors[i] == colors[i + 2] and colors[i] != colors[i + 1]:
            result += 1
    return result


if __name__ == "__main__":
    assert number_of_alternating_groups(colors=[1, 1, 1]) == 0
    assert number_of_alternating_groups(colors=[0, 1, 0, 0, 1]) == 3
