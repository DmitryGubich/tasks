def count_homogenous(s: str) -> int:
    left = 0
    res = 0

    for right in range(len(s)):
        if s[left] == s[right]:
            res += right - left + 1
        else:
            res += 1
            left = right

    return res % (10**9 + 7)


if __name__ == "__main__":
    assert count_homogenous(s="abbcccaa") == 13
    assert count_homogenous(s="xy") == 2
    assert count_homogenous(s="zzzzz") == 15
