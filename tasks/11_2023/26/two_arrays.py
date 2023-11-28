def two_arrays_1(arr1: list[str], arr2: list[str]) -> int:
    # O(arr1 * arr2) Time
    # O(1) Space

    for i in arr1:
        for j in arr2:
            if i == j:
                return True
    return False


def two_arrays_2(arr1: list[str], arr2: list[str]) -> int:
    # O(arr1 + arr2)
    # O(arr1) Space

    hashset = set()
    for i in arr1:
        hashset.add(i)
    for j in arr2:
        if j in hashset:
            return True
    return False


def two_arrays_3(arr1: list[str], arr2: list[str]) -> int:
    # O(arr1 + arr2)
    # O(1) Space

    for i in arr1:
        if i in arr2:
            return True
    return False


if __name__ == "__main__":
    assert two_arrays_1(arr1=["a", "b", "t", "x"], arr2=["z", "y", "c"]) is False
    assert two_arrays_1(arr1=["a", "b", "t", "x"], arr2=["z", "y", "x"]) is True

    assert two_arrays_2(arr1=["a", "b", "t", "x"], arr2=["z", "y", "c"]) is False
    assert two_arrays_2(arr1=["a", "b", "t", "x"], arr2=["z", "y", "x"]) is True

    assert two_arrays_3(arr1=["a", "b", "t", "x"], arr2=["z", "y", "c"]) is False
    assert two_arrays_3(arr1=["a", "b", "t", "x"], arr2=["z", "y", "x"]) is True
