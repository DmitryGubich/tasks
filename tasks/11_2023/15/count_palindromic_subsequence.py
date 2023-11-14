import itertools


def count_palindromic_subsequence(input_string: str) -> int:
    result = 0
    for combination in set(itertools.combinations(input_string, r=3)):
        if combination == combination[::-1]:
            result += 1
    return result


if __name__ == "__main__":
    assert count_palindromic_subsequence(input_string="aabca") == 3
    assert count_palindromic_subsequence(input_string="adc") == 0
    assert count_palindromic_subsequence(input_string="bbcbaba") == 4
