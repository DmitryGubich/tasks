def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])


if __name__ == "__main__":
    assert length_of_last_word(s="Hello World") == 5
    assert length_of_last_word(s="   fly me   to   the moon  ") == 4
    assert length_of_last_word(s="luffy is still joyboy") == 6
