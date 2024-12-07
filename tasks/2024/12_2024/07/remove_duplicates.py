def remove_duplicates(s: str) -> str:
    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)


if __name__ == "__main__":
    assert remove_duplicates(s="abbaca") == "ca"
    assert remove_duplicates(s="azxxzy") == "ay"
