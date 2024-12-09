def permute(nums: list[int]) -> list[list[int]]:
    def back_tracking(nums: list[int], current: list[int]):
        if len(nums) == len(current):
            result.append(list(current))
            return
        for i in nums:
            if i not in current:
                current.append(i)
                back_tracking(nums, current)
                current.pop()

    result = []
    back_tracking(nums, [])
    return result


if __name__ == "__main__":
    assert permute(nums=[1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert permute(nums=[0, 1]) == [[0, 1], [1, 0]]
