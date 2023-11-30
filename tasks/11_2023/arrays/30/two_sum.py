def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, element in enumerate(nums):
        compliment = target - element
        if hashmap.get(compliment) is not None:
            return [hashmap.get(compliment) + 1, i + 1]
        hashmap[element] = i


if __name__ == "__main__":
    assert two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum(nums=[3, 2, 4], target=6) == [1, 2]
