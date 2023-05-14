# Implement compress() and decompress() functions for a basic string compression scheme.
# In particular, we would like to compress strings with long runs of the same character, for example "aaabbbbbbccdddd".

from itertools import groupby


def compress(data):
    compressed_seq = ""
    compressed = [(x, len(list(y))) for x, y in groupby(data)]
    for _, elem in enumerate(compressed):
        for j in elem:
            if j != 1:
                compressed_seq += str(j)
    return compressed_seq
    # result = ""
    # counter = 1
    # for i, letter in enumerate(s):
    #     try:
    #         next_symbol = s[i + 1]
    #     except IndexError:
    #         result = update_result_string(counter, letter, result)
    #     if next_symbol == letter:
    #         counter += 1
    #     if next_symbol != letter:
    #         result = update_result_string(counter, letter, result)
    #         counter = 1
    # return result


# def update_result_string(counter, letter, result):
#     if counter == 1:
#         result += letter
#     else:
#         result += f"{counter}{letter}"
#     return result


if __name__ == "__main__":
    assert "abc" == compress("abc")
    assert "a3gb6c2d4f" == compress("aaagbbbbbbccddddf")
    assert "a3b6c2a3d4f" == compress("aaabbbbbbccaaaddddf")
