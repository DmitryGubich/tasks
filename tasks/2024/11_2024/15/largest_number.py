def largest_number(nums: list[int]) -> str:
    array = list(map(str, nums))
    array.sort(key=lambda x: x * 10, reverse=True)
    if array[0] == "0":
        return "0"
    largest = "".join(array)
    return largest


if __name__ == "__main__":
    assert largest_number(nums=[10, 2]) == "210"
    assert largest_number(nums=[3, 30, 34, 5, 9]) == "9534330"
