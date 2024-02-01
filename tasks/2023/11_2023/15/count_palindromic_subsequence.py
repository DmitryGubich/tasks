def count_palindromic_subsequence(input_string: str) -> int:
    res = 0
    uniq = set(input_string)

    for c in uniq:
        start = input_string.find(c)
        end = input_string.rfind(c)

        if start < end:
            res += len(set(input_string[start + 1 : end]))

    return res


if __name__ == "__main__":
    assert count_palindromic_subsequence(input_string="aabca") == 3
    assert count_palindromic_subsequence(input_string="adc") == 0
    assert count_palindromic_subsequence(input_string="bbcbaba") == 4
