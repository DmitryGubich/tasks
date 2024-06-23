def number_of_subarrays(nums: list[int], k: int) -> int:
    result, left, counter = 0, 0, 0

    for right in range(len(nums)):
        if nums[right] % 2:
            k -= 1
            counter = 0
        while not k:
            k += nums[left] % 2
            counter += 1
            left += 1
        result += counter
    return result


if __name__ == "__main__":
    assert number_of_subarrays(nums=[1, 1, 2, 1, 1], k=3) == 2
    assert number_of_subarrays(nums=[2, 4, 6], k=1) == 0
