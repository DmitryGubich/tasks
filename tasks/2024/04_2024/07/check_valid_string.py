def check_valid_string(s: str) -> int:
    left, ast = [], []

    for i, char in enumerate(s):
        if char == "(":
            left.append(i)
        elif char == "*":
            ast.append(i)
        elif left:
            left.pop()
        elif ast:
            ast.pop()
        else:
            return False

    while left and ast and left[-1] < ast[-1]:
        left.pop()
        ast.pop()

    return not left


if __name__ == "__main__":
    assert check_valid_string(s="()") is True
    assert check_valid_string(s="(*))") is True
