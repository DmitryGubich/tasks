# PIN
def calculate_scores(nums: list[int], target: int) -> int:
    left = answer = 0
    current = []

    for right in range(len(nums)):
        current.append(nums[right])
        while sum(current) * len(current) > target:
            current.remove(nums[left])
            left += 1
        answer += len(current)
    return answer


if __name__ == "__main__":
    assert calculate_scores(nums=[2, 1, 3, 4, 5], target=6) == 6
    assert calculate_scores(nums=[1, 1, 1], target=5) == 5
