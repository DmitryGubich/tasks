def check_arithmetic_subarrays(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    def check_arithmetic_array(sub: list[int]) -> bool:
        sub.sort()
        dif = sub[1] - sub[0]
        for i in range(2, len(sub)):
            if sub[i] - sub[i - 1] != dif:
                return False
        return True

    res = []
    for q in range(len(l)):
        res.append(check_arithmetic_array(nums[l[q] : r[q] + 1]))
    return res


if __name__ == "__main__":
    assert check_arithmetic_subarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]) == [
        True,
        False,
        True,
    ]
