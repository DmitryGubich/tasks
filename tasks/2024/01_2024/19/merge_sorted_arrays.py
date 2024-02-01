def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    return arr


if __name__ == "__main__":
    assert merge_sorted_arrays(arr1=[1, 3, 5], arr2=[2, 4, 6]) == [1, 2, 3, 4, 5, 6]
