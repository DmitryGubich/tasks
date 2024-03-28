def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0
    left = ans = 0
    cur = 1
    for right in range(len(nums)):
        cur *= nums[right]
        while cur >= k:
            cur //= nums[left]
            left += 1
        ans += right - left + 1

    return ans


if __name__ == "__main__":
    assert num_subarray_product_less_than_k(nums=[10, 5, 2, 6], k=100) == 8
    assert num_subarray_product_less_than_k(nums=[1, 2, 3], k=0) == 0
