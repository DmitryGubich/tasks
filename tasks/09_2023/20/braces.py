def check_braces(s: str) -> bool:
    braces_map = {
        "{": "}",
        "(": ")",
        "[": "]",
    }

    stack = []
    for i in s:
        if i in braces_map:
            stack.append(i)
        else:
            brace = stack.pop()
            if i != braces_map.get(brace):
                return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    assert check_braces(s="{({})}") is True
    assert check_braces(s="{[]()}") is True
    assert check_braces(s="[()]{}{[()()]()}") is True
    assert check_braces(s="{([})}") is False
    assert check_braces(s="[(])") is False
