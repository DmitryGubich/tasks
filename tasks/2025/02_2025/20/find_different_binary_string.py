def find_different_binary_string(nums: list[str]) -> str:
    size = len(nums)
    nums.sort()
    pointer = 0

    for i in range(size):
        decimal_value = int(nums[i], 2)

        if decimal_value == pointer:
            pointer += 1
        else:
            return format(pointer, f"0{size}b")

    return format(pointer, f"0{size}b")


if __name__ == "__main__":
    assert find_different_binary_string(nums=["00", "10"]) == "01"
    assert find_different_binary_string(nums=["111", "011", "001"]) == "000"
