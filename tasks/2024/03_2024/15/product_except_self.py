from functools import reduce


def product_except_self(nums: list[int]) -> list[int]:
    prod = reduce(lambda x, y: x * y, nums)
    result = [0] * len(nums)
    for i, num in enumerate(nums):
        result[i] = int(prod / num)
    return result


if __name__ == "__main__":
    assert product_except_self(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
