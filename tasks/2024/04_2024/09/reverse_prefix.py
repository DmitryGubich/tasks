def reverse_prefix(word: str, ch: str) -> str:
    result = ""
    for i, val in enumerate(word):
        if val == ch:
            result = val + result[::-1]
            break
        else:
            result += val

    return result + word[i + 1 :]


if __name__ == "__main__":
    assert reverse_prefix(word="abcdefd", ch="d") == "dcbaefd"
    assert reverse_prefix(word="xyxzxe", ch="z") == "zxyxxe"
