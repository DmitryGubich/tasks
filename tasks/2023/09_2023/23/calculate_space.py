def calculate_space(first_coordinates: list[int], second_coordinates: list[int]) -> int:
    x1, y1, x2, y2 = first_coordinates
    x3, y3, x4, y4 = second_coordinates
    return (
        max(
            max(x1, x2, x3, x4) - min(x1, x2, x3, x4),
            max(y1, y2, y3, y4) - min(y1, y2, y3, y4),
        )
        ** 2
    )


if __name__ == "__main__":
    assert calculate_space(first_coordinates=[6, 6, 8, 8], second_coordinates=[1, 8, 4, 9]) == 49
    assert calculate_space(first_coordinates=[6, 6, 8, 8], second_coordinates=[1, 1, 4, 9]) == 64
    assert calculate_space(first_coordinates=[6, 6, 8, 8], second_coordinates=[8, 3, 10, 5]) == 25
