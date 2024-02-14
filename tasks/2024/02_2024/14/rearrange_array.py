def rearrange_array(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * n
    pos, neg = 0, 1
    for num in nums:
        if num < 0:
            ans[neg] = num
            neg += 2
        else:
            ans[pos] = num
            pos += 2

    return ans


if __name__ == "__main__":
    assert rearrange_array(nums=[3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
    assert rearrange_array(nums=[-1, 1]) == [1, -1]
