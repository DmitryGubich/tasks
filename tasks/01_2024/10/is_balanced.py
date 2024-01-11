def is_balanced(s: str) -> bool:
    braces = {
        "{": "}",
        "[": "]",
        "(": ")",
    }
    stack = []

    for i in s:
        if i in braces:
            stack.append(i)
        else:
            if not stack or braces.get(stack.pop()) != i:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    assert is_balanced(s="{[()]}") is True
    assert is_balanced(s="{[(]}") is False
    assert is_balanced(s="}][}}(}][))]") is False
