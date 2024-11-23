def maximum_subarray_sum(nums: list[int], k: int) -> int:
    seen = set()
    cur_sum = max_sum = left = cur_len = 0
    for right in range(len(nums)):
        cur_sum += nums[right]
        while left < right and (cur_len > k - 1 or nums[right] in seen):
            seen.remove(nums[left])
            cur_sum -= nums[left]
            left += 1
            cur_len -= 1
        seen.add(nums[right])
        cur_len += 1
        if cur_len == k:
            max_sum = max(max_sum, cur_sum)
    return max_sum


if __name__ == "__main__":
    assert maximum_subarray_sum(nums=[3, 5, 3, 4], k=2) == 8
    assert maximum_subarray_sum(nums=[1, 2, 2], k=2) == 3
    assert maximum_subarray_sum(nums=[1, 5, 4, 2, 9, 9, 9], k=3) == 15
    assert maximum_subarray_sum(nums=[4, 4, 4], k=3) == 0
    assert maximum_subarray_sum(nums=[1, 2, 2], k=2) == 3
