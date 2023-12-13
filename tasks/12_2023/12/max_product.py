def max_product(nums: list[int]) -> int:
    first, second = 0, 0

    for number in nums:
        if number > first:
            first, second = number, first
        elif number > second:
            second = number

    return (first - 1) * (second - 1)


if __name__ == "__main__":
    assert max_product(nums=[3, 4, 5, 2]) == 12
    assert max_product(nums=[1, 5, 4, 5]) == 16
