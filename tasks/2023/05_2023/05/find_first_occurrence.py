def find_first_occurrence(haystack: str, needle: str) -> int:
    # return haystack.find(needle)
    if needle in haystack:
        for i, _ in enumerate(haystack):
            if needle == haystack[i : i + len(needle)]:
                return i
    else:
        return -1


if __name__ == "__main__":
    assert find_first_occurrence(haystack="sadbutsad", needle="sad") == 0
    assert find_first_occurrence(haystack="leetcode", needle="leeto") == -1
    assert find_first_occurrence(haystack="hello", needle="ll") == 2
