def sort_colors(nums: list[int]) -> None:
    hash_map = {0: 0, 1: 0, 2: 0}

    for i in nums:
        hash_map[i] += 1

    index = 0

    for color in range(3):
        while hash_map[color] > 0:
            nums[index] = color
            index += 1
            hash_map[color] -= 1


if __name__ == "__main__":
    colors = [2, 0, 2, 1, 1, 0]
    sort_colors(nums=colors)
    assert colors == [0, 0, 1, 1, 2, 2]
