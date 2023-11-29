def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


if __name__ == "__main__":
    assert merge_sorted_arrays(arr1=[3, 4, 8], arr2=[4, 6, 9]) == [3, 4, 4, 6, 8, 9]
    assert merge_sorted_arrays(arr1=[0, 3], arr2=[4, 6, 30, 31]) == [0, 3, 4, 6, 30, 31]
    assert merge_sorted_arrays(arr1=[], arr2=[4, 6, 30, 31]) == [4, 6, 30, 31]
    assert merge_sorted_arrays(arr1=[4, 6, 30, 31], arr2=[0, 3]) == [0, 3, 4, 6, 30, 31]
