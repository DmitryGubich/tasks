def frequency_sort(s: str) -> str:
    hashmap = {}
    for i in s:
        if hashmap.get(i):
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    result = ""
    for k in sorted(hashmap.keys(), key=lambda x: -hashmap[x]):
        result += k * hashmap[k]

    return result


if __name__ == "__main__":
    assert frequency_sort(s="tree") == "eetr"
    assert frequency_sort(s="cccaaa") == "cccaaa"
