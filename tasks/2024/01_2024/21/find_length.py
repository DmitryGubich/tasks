def find_length(nums: list[int], k: int) -> int:
    left = answer = current = 0

    for right in range(len(nums)):
        current += nums[right]
        while current > k:
            current -= nums[left]
            left += 1
        answer = max(answer, right - left + 1)

    return answer


if __name__ == "__main__":
    assert find_length(nums=[3, 1, 2, 7, 4, 2, 1, 1, 5], k=8) == 4
