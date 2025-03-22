def get_concatenation(nums: list[int]) -> list[int]:
    ans = []
    for _ in range(2):
        for i in nums:
            ans.append(i)

    return ans


if __name__ == "__main__":
    assert get_concatenation(nums=[1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert get_concatenation(nums=[1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
