from typing import List, Set


def common_chars(words: List[str]) -> Set[str]:
    return set.intersection(*map(set, words))


if __name__ == "__main__":
    assert common_chars(words=["bella", "label", "roller"]) == {"e", "l"}
    assert common_chars(words=["cool", "lock", "cook"]) == {"c", "o"}
