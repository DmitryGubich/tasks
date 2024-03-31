def count_fixed_subarrays(nums: list[int], min_k: int, max_k: int) -> int:
    count = 0
    min_idx = max_idx = left_idx = -1

    for right_idx, num in enumerate(nums):
        if num < min_k or num > max_k:
            left_idx = right_idx

        if num == min_k:
            min_idx = right_idx
        if num == max_k:
            max_idx = right_idx

        count += max(0, min(min_idx, max_idx) - left_idx)

    return count


if __name__ == "__main__":
    assert count_fixed_subarrays(nums=[1, 3, 5, 2, 7, 5], min_k=1, max_k=5) == 2
    assert count_fixed_subarrays(nums=[1, 1, 1, 1], min_k=1, max_k=1) == 10
