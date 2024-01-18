def compress_string(data: str) -> str:
    result = ""
    counter = 1
    for i in range(0, len(data) - 1):
        letter = data[i]
        next_letter = data[i + 1]
        if letter == next_letter:
            counter += 1
        else:
            result += letter if counter == 1 else f"{letter}{counter}"
            counter = 1

    result += next_letter if counter == 1 else f"{next_letter}{counter}"
    return result


if __name__ == "__main__":
    assert compress_string("abc") == "abc"
    assert compress_string("ffaaa") == "f2a3"
    assert compress_string("aaa") == "a3"
    assert compress_string("aaagbbbbbbccddddf") == "a3gb6c2d4f"
    assert compress_string("aaabbbbbbccaaaddddf") == "a3b6c2a3d4f"
