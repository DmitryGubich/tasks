def get_number_of_good_pairs(size: int, numbers: list[int]) -> int:
    m = [0] * 200
    for i in numbers:
        m[i % 200] += 1
    return sum(x * (x - 1) // 2 for x in m)


if __name__ == "__main__":
    assert get_number_of_good_pairs(size=5, numbers=[203, 404, 204, 200, 403]) == 2
    assert get_number_of_good_pairs(size=1, numbers=[1000000]) == 0
    assert get_number_of_good_pairs(size=3, numbers=[2022, 2020, 2021]) == 0
