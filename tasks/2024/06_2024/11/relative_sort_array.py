from collections import defaultdict


def relative_sort_array(arr1: list[int], arr2: list[int]) -> list[int]:
    count_map = defaultdict(int)
    remaining = []
    result = []

    for num in arr2:
        count_map[num] = 0

    for num in arr1:
        if num in count_map:
            count_map[num] += 1
        else:
            remaining.append(num)

    remaining.sort()

    for num in arr2:
        result.extend([num] * count_map[num])

    result.extend(remaining)
    return result


if __name__ == "__main__":
    assert relative_sort_array(
        arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]
    ) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
