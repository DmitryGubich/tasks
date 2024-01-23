def find_best_subarray(nums: list[int], k: int) -> int:
    current = sum(nums[:k])
    answer = current
    for i in range(k, len(nums)):
        current += nums[i] - nums[k - i]
        answer = max(answer, current)

    return answer


if __name__ == "__main__":
    assert find_best_subarray(nums=[3, -1, 4, 12, -8, 5, 6], k=4) == 18
