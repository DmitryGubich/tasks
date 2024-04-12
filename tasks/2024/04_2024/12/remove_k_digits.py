def remove_k_digits(num: str, k: int) -> str:
    stack = []
    for n in num:
        while stack and k and stack[-1] > n:
            stack.pop()
            k -= 1

        if stack or n != "0":
            stack.append(n)

    if k:
        stack = stack[0:-k]

    return "".join(stack) or "0"


if __name__ == "__main__":
    assert remove_k_digits(num="1432219", k=3) == "1219"
    assert remove_k_digits(num="10200", k=1) == "200"
