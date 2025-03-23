def k_largest_pair_sum_brute(nums: list[int], k: int) -> int:
    sums = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sums.append(nums[i] + nums[j])

    return sorted(sums, reverse=True)[k - 1]


if __name__ == "__main__":
    assert k_largest_pair_sum_brute(nums=[1, 2, 3, 5], k=3) == 6
    assert k_largest_pair_sum_brute(nums=[4, 2, 5, 5], k=3) == 9
