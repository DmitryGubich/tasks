def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if anagrams.get(sorted_word):
            anagrams.get(sorted_word).append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


if __name__ == "__main__":
    assert group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"],
    ]
    assert group_anagrams(strs=["a"]) == [["a"]]
