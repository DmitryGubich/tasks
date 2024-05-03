def reverse_prefix(word: str, ch: str) -> str:
    result = ""
    i = 0

    for i in range(len(word)):
        if word[i] == ch:
            result = word[i] + result[::-1]
            break
        else:
            result += word[i]

    for j in range(i + 1, len(word)):
        result += word[j]

    return result


if __name__ == "__main__":
    assert reverse_prefix(word="abcdefd", ch="d") == "dcbaefd"
    assert reverse_prefix(word="xyxzxe", ch="z") == "zxyxxe"
