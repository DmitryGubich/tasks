from typing import List


def merge_two_lists(list1: List, list2: List) -> List:
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    if list1 or list2:
        result += list1 if list1 else list2
    return result


if __name__ == "__main__":
    assert [1, 1, 2, 3, 4, 4] == merge_two_lists(list1=[1, 2, 4], list2=[1, 3, 4])
    assert [1, 3, 4, 5, 6, 7] == merge_two_lists(list1=[5, 6, 7], list2=[1, 3, 4])
    assert [1, 3, 4, 5, 6, 7] == merge_two_lists(list1=[1, 3, 4], list2=[5, 6, 7])
