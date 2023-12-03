def array_strings_are_equal(word1: list[str], word2: list[str]) -> bool:
    return "".join(word1) == "".join(word2)


if __name__ == "__main__":
    assert array_strings_are_equal(word1=["abc", "d", "de"], word2=["abcdde"]) is True
    assert array_strings_are_equal(word1=["a", "cb"], word2=["ab", "c"]) is False
