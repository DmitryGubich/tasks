def sort_vowels(input_string: str) -> str:
    result = list(input_string)
    vowels_indexes, vowels_letters = [], []

    for index, char in enumerate(input_string):
        if char.lower() in {"a", "e", "i", "o", "u"}:
            vowels_indexes.append(index)
            vowels_letters.append(char)

    for letter in sorted(vowels_letters):
        result[vowels_indexes.pop(0)] = letter

    return "".join(result)


if __name__ == "__main__":
    assert sort_vowels(input_string="lEetcOde") == "lEOtcede"
    assert sort_vowels(input_string="lYmpH") == "lYmpH"
