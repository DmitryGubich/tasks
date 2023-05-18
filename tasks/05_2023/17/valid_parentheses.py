def valid_parentheses(s: str) -> bool:
    d = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0


if __name__ == "__main__":
    assert valid_parentheses(s=")(") is False
    assert valid_parentheses(s="()") is True
    assert valid_parentheses(s="()[]{}") is True
    assert valid_parentheses(s="(]") is False
    assert valid_parentheses(s="([)]") is False
    assert valid_parentheses(s="{[]}") is True
