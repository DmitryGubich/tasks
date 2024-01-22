def subarray_product_less(nums: list[int], k: int) -> int:
    left = answer = 0
    current = 1

    for right in range(len(nums)):
        current *= nums[right]
        while current >= k:
            current //= nums[left]
            left += 1
        answer += right - left + 1

    return answer


if __name__ == "__main__":
    assert subarray_product_less(nums=[10, 5, 2, 6], k=100) == 8
