def max_repeating(sequence: str, word: str) -> int:
    result = 1
    while word * result in sequence:
        result += 1
    return result - 1

    # k = len(word)
    # result, i = 0, 0
    # while i <= len(sequence):
    #     sub = sequence[i : i + k]
    #     if sub == word:
    #         i += k
    #         result += 1
    #     else:
    #         i += 1
    # return result


if __name__ == "__main__":
    assert max_repeating(sequence="ababc", word="ab") == 2
    assert max_repeating(sequence="ababc", word="ba") == 1
