def minimum_common_value(nums1: list[int], nums2: list[int]) -> int:
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            return nums1[i]

    return -1


if __name__ == "__main__":
    assert minimum_common_value(nums1=[1, 2, 3], nums2=[2, 4]) == 72
    assert minimum_common_value(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]) == 2
