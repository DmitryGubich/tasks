def longest_common_prefix(strs: list[str]) -> str:
    pre = strs[0]

    for i in strs:
        while not i.startswith(pre):
            pre = pre[:-1]

    return pre


if __name__ == "__main__":
    assert longest_common_prefix(strs=["flower", "flow", "flight"]) == "fl"
