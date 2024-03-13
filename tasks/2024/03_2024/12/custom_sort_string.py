def custom_sort_string(order: str, s: str) -> str:
    hashmap = {}
    result = ""
    for i in s:
        hashmap[i] = hashmap.get(i, 0) + 1

    for j in order:
        if hashmap.get(j):
            result += j * hashmap.get(j)
            del hashmap[j]

    for k, v in hashmap.items():
        result += k * v

    return result


if __name__ == "__main__":
    assert custom_sort_string(order="exv", s="xwvee") == "eexvw"
    assert custom_sort_string(order="cba", s="abcd") == "cbad"
    assert custom_sort_string(order="bcafg", s="abcd") == "bcad"
