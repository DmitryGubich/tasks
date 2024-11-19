def maximum_subarray_sum(nums: list[int], k: int) -> int:
    result = 0
    cur_sum = 0
    res = set()

    for i in range(len(nums)):
        if nums[i] not in res:
            if len(res) < k:
                res.add(nums[i])
                cur_sum += nums[i]
            if len(res) == k:
                result = max(result, cur_sum)
                cur_sum -= nums[i - k + 1]
                res.remove(nums[i - k + 1])
        else:
            res = {nums[i - 1], nums[i]}
            cur_sum = sum(res)
    return result


if __name__ == "__main__":
    assert maximum_subarray_sum(nums=[3, 5, 3, 4], k=2) == 8
    assert maximum_subarray_sum(nums=[1, 2, 2], k=2) == 3
    assert maximum_subarray_sum(nums=[1, 5, 4, 2, 9, 9, 9], k=3) == 15
    assert maximum_subarray_sum(nums=[4, 4, 4], k=3) == 0
    assert maximum_subarray_sum(nums=[1, 2, 2], k=2) == 3
