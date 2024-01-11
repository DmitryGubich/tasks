def icecream_parlor(m: int, arr: list) -> list:
    hashmap = {}
    for i, elem in enumerate(arr):
        compliment = m - elem
        if hashmap.get(compliment) is not None:
            return [hashmap.get(compliment) + 1, i + 1]
        hashmap[elem] = i


def icecream_parlor_bool(m: int, arr: list) -> bool:
    hashset = set()
    for elem in arr:
        compliment = m - elem
        if compliment in hashset:
            return True
        hashset.add(elem)
    return False


if __name__ == "__main__":
    assert icecream_parlor(m=4, arr=[1, 2, 5, 3, 1]) == [1, 4]
    assert icecream_parlor(m=4, arr=[2, 2, 4, 3]) == [1, 2]

    assert icecream_parlor_bool(m=4, arr=[1, 2, 5, 3, 1]) is True
    assert icecream_parlor_bool(m=4, arr=[2, 4, 4, 3]) is False
