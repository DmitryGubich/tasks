def height_checker(heights: list[int]) -> int:
    result = 0
    sorted_heights = sorted(heights)
    for i in range(len(sorted_heights)):
        result += sorted_heights[i] != heights[i]
    return result


if __name__ == "__main__":
    assert height_checker(heights=[1, 1, 4, 2, 1, 3]) == 3
    assert height_checker(heights=[5, 1, 2, 3, 4]) == 5
