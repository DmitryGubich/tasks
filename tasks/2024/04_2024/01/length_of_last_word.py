def length_of_last_word(s: str) -> int:
    result = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            result += 1
        elif result:
            return result

    return result


if __name__ == "__main__":
    assert length_of_last_word(s="a") == 1
    assert length_of_last_word(s="Hello World") == 5
    assert length_of_last_word(s="   fly me   to   the moon  ") == 4
