def max_subarray_length(nums: list[int], k: int) -> int:
    left = ans = 0
    hash_map = {}
    for right in range(len(nums)):
        hash_map[nums[right]] = hash_map.get(nums[right], 0) + 1
        while hash_map[nums[right]] > k:
            hash_map[nums[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans


if __name__ == "__main__":
    assert max_subarray_length(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2) == 6
    assert max_subarray_length(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1) == 2
    assert max_subarray_length(nums=[3, 1, 1], k=1) == 2
