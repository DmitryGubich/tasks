def max_depth(s: str) -> int:
    count = result = 0
    for i in s:
        if i == "(":
            count += 1
            result = max(result, count)
        elif i == ")":
            count -= 1
    return result


if __name__ == "__main__":
    assert max_depth(s="(1+(2*3)+((8)/4))+1") == 3
    assert max_depth(s="(1)+((2))+(((3)))") == 3
