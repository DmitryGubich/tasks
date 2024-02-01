def reverse_string_recursive(word: str) -> str:
    if len(word) == 1:
        return word
    return reverse_string_recursive(word[1:]) + word[0]


if __name__ == "__main__":
    assert reverse_string_recursive("hey") == "yeh"
