def longest_common_prefix(strs: list[str]) -> str:
    result = ""

    for i in range(len(min(strs))):
        symbol = strs[0][i]

        for j in range(1, len(strs)):
            if strs[j][i] != symbol:
                return result

        result += symbol

    return result


if __name__ == "__main__":
    assert longest_common_prefix(strs=["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(strs=["flower", "flower", "flower"]) == "flower"
