def find_closest_number(nums: list[int]) -> int:
    closest_number = nums[0]

    for num in nums:
        if abs(num) < abs(closest_number):
            closest_number = num

    if closest_number < 0 and abs(closest_number) in nums:
        return abs(closest_number)
    return closest_number


if __name__ == "__main__":
    assert find_closest_number(nums=[-4, -2, 1, 4, 8]) == 1
    assert find_closest_number(nums=[2, -1, 1]) == 1
