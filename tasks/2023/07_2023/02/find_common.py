def find_common(nums1: list[int], nums2: list[int], nums3: list[int]) -> int:
    i, j, k = 0, 0, 0
    n1, n2, n3 = len(nums1), len(nums2), len(nums3)

    while i < n1 and j < n2 and k < n3:
        if nums1[i] == nums2[j] and nums2[j] == nums3[k]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums2[j] < nums3[k]:
            j += 1
        else:
            k += 1


if __name__ == "__main__":
    assert find_common([1, 2, 4, 5], [3, 3, 4], [2, 3, 4, 5, 6]) == 4
