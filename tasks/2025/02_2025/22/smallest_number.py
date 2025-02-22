def smallest_number(pattern: str) -> str:
    result = []
    stack = []

    for index in range(len(pattern) + 1):
        stack.append(index + 1)
        if index == len(pattern) or pattern[index] == "I":
            while stack:
                result.append(str(stack.pop()))
    return "".join(result)


if __name__ == "__main__":
    assert smallest_number(pattern="IIIDIDDD") == "123549876"
    assert smallest_number(pattern="DDDI") == "43215"
