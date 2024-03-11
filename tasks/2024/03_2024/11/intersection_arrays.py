def intersection_arrays(nums1: list[int], nums2: list[int]) -> list[int]:
    hashmap = {}
    for i in set(nums1):
        hashmap[i] = hashmap.get(i, 0) + 1
    for j in set(nums2):
        hashmap[j] = hashmap.get(j, 0) + 1

    return [k for k, v in hashmap.items() if v == 2]
    # return set(nums1) & set(nums2)


if __name__ == "__main__":
    assert intersection_arrays(nums1=[1, 2, 2, 1], nums2=[2, 2]) == [2]
    assert intersection_arrays(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [9, 4]
