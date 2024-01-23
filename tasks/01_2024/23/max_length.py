def max_length(arr: list[str]) -> int:
    result = 0
    unique = [""]

    for word in arr:
        for j in unique:
            tmp = word + j
            if len(tmp) == len(set(tmp)):
                unique.append(tmp)
                result = max(result, len(tmp))

    return result


if __name__ == "__main__":
    assert max_length(arr=["un", "iq", "ue"]) == 4
    assert max_length(arr=["cha", "r", "act", "ers"]) == 6
