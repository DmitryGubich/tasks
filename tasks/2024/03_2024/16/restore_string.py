def restore_string(s: str, indices: list[int]) -> str:
    result = ["*"] * len(s)
    for i, char in enumerate(s):
        result[indices[i]] = char
        i += 1
    return "".join(result)


if __name__ == "__main__":
    assert restore_string(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"
