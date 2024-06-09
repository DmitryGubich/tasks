def subarrays_div_by_k(nums: list[int], k: int) -> int:
    hash_map = {0: 1}
    sums, result = 0, 0
    for i in range(len(nums)):
        sums += nums[i]
        if sums % k in hash_map:
            result += hash_map[sums % k]
        hash_map[sums % k] = hash_map.get(sums % k, 0) + 1
    return result


if __name__ == "__main__":
    assert subarrays_div_by_k(nums=[4, 5, 0, -2, -3, 1], k=5) == 7
    assert subarrays_div_by_k(nums=[5], k=9) == 0
