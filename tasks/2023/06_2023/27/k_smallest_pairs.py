def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    result = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            result.append([nums1[i], nums2[j]])
    result = sorted(result, key=lambda x: x[0] + x[1])
    return result[:k]


if __name__ == "__main__":
    assert k_smallest_pairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3) == [
        [1, 2],
        [1, 4],
        [1, 6],
    ]
    assert k_smallest_pairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2) == [[1, 1], [1, 1]]
    assert k_smallest_pairs(nums1=[1, 2], nums2=[3], k=3) == [[1, 3], [2, 3]]
