def majority_element(nums: list[int]) -> list[int]:
    count = {}
    threshold = len(nums) // 3
    majority_elements = []
    for i in nums:
        count[i] = count.get(i, 0) + 1
        if count[i] > threshold:
            majority_elements.append(i)
    return list(set(majority_elements))


if __name__ == "__main__":
    assert majority_element(nums=[3, 2, 3]) == [3]
    assert majority_element(nums=[1, 2]) == [1, 2]
    assert majority_element(nums=[1]) == [1]
    assert majority_element(nums=[2, 2]) == [2]
