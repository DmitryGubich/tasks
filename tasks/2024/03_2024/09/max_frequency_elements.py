def max_frequency_elements(nums: list[int]) -> int:
    hashmap = {}
    max_el = result = 0
    for i in nums:
        hashmap[i] = hashmap.get(i, 0) + 1

    for value in hashmap.values():
        if value > max_el:
            max_el = value
            result = max_el
        elif value == max_el:
            result += max_el
    return result


if __name__ == "__main__":
    assert max_frequency_elements(nums=[1, 2, 2, 3, 1, 4]) == 4
    assert max_frequency_elements(nums=[1, 2, 3, 4, 5]) == 5
