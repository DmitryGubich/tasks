from typing import List


def find_median(nums1: List[int], nums2: List[int]) -> float:
    result = sorted(nums1 + nums2)
    central_index = int(len(result) / 2)
    median = result[central_index]

    if len(result) % 2 == 0:
        median = (median + result[central_index - 1]) / 2

    return median


if __name__ == '__main__':
    assert 2.00000 == find_median(nums1=[1, 3], nums2=[2])
    assert 2.50000 == find_median(nums1=[1, 2], nums2=[3, 4])
