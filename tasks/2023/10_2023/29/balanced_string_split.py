def balanced_string_split(s: str) -> int:
    c = result = 0
    for i in s:
        if i == "R":
            c += 1
        else:
            c -= 1
        if c == 0:
            result += 1
    return result


if __name__ == "__main__":
    assert balanced_string_split(s="RLRRLLRLRL") == 4
    assert balanced_string_split(s="RLRRRLLRLL") == 2
    assert balanced_string_split(s="LLLLRRRR") == 1
