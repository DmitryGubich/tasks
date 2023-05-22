from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    frequency = {}
    for i in nums:
        if frequency.get(i):
            frequency[i] += 1
        else:
            frequency[i] = 1
    return sorted(frequency, key=frequency.get, reverse=True)[:k]


if __name__ == "__main__":
    assert [1, 2] == top_k_frequent(nums=[1, 1, 1, 1, 2, 2, 3], k=2)
    assert [1] == top_k_frequent(nums=[1], k=1)
