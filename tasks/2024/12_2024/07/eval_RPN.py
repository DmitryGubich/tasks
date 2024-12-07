def eval_RPN(tokens: list[str]) -> int:
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: int(x / y),
        "*": lambda x, y: x * y,
    }
    stack = []
    for token in tokens:
        if token not in "+-/*":
            stack.append(int(token))
        else:
            i1 = stack.pop()
            i2 = stack.pop()
            stack.append(operations[token](i2, i1))
    return stack.pop()


if __name__ == "__main__":
    assert eval_RPN(tokens=["2", "1", "-", "3", "*"]) == 3
    assert eval_RPN(tokens=["4", "13", "5", "/", "+"]) == 6
