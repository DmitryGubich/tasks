def count_subarrays(nums: list[int], k: int) -> int:
    max_elem = max(nums)
    left = ans = count = 0
    for right in range(len(nums)):
        if nums[right] == max_elem:
            count += 1
        while count >= k:
            if nums[left] == max_elem:
                count -= 1
            left += 1
        ans += left
    return ans


if __name__ == "__main__":
    assert count_subarrays(nums=[1, 3, 2, 3, 3], k=2) == 6
    assert count_subarrays(nums=[1, 4, 2, 1], k=3) == 0
