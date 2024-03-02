def sorted_squares(nums: list[int]) -> list[int]:
    return sorted([i**2 for i in nums])


if __name__ == "__main__":
    assert sorted_squares(nums=[-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert sorted_squares(nums=[-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
