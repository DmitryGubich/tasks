def is_isomorphic(s: str, t: str) -> bool:
    map_1 = []
    map_2 = []
    for i in s:
        map_1.append(s.index(i))
    for i in t:
        map_2.append(t.index(i))

    return map_1 == map_2


if __name__ == "__main__":
    assert is_isomorphic(s="egg", t="add") is True
    assert is_isomorphic(s="foo", t="bar") is False
    assert is_isomorphic(s="paper", t="title") is True
