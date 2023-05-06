def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])


if __name__ == "__main__":
    assert 5 == length_of_last_word(s="Hello World")
    assert 4 == length_of_last_word(s="   fly me   to   the moon  ")
    assert 6 == length_of_last_word(s="luffy is still joyboy")
