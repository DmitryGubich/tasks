def find_first_occurrence(haystack: str, needle: str) -> int:
    # return haystack.find(needle)
    if needle in haystack:
        for i, _ in enumerate(haystack):
            if needle == haystack[i : i + len(needle)]:
                return i
    else:
        return -1


if __name__ == "__main__":
    assert 0 == find_first_occurrence(haystack="sadbutsad", needle="sad")
    assert -1 == find_first_occurrence(haystack="leetcode", needle="leeto")
    assert 2 == find_first_occurrence(haystack="hello", needle="ll")
