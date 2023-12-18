def max_product_difference(nums: list[int]) -> int:
    first_big = second_big = 0
    first_small = second_small = float("inf")

    for n in nums:
        if n < first_small:
            first_small, second_small = n, first_small
        elif n < second_small:
            second_small = n

        if n > first_big:
            first_big, second_big = n, first_big
        elif n > second_big:
            second_big = n

    return first_big * second_big - first_small * second_small


if __name__ == "__main__":
    assert max_product_difference(nums=[5, 6, 2, 7, 4]) == 34
    assert max_product_difference(nums=[4, 2, 5, 9, 7, 4, 8]) == 64
