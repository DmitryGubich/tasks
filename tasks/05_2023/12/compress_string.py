# Implement compress() and decompress() functions for a basic string compression scheme.
# In particular, we would like to compress strings with long runs of the same character, for example "aaabbbbbbccdddd".


def compress(s):
    result = ""
    counter = 1
    for i, letter in enumerate(s):
        try:
            next_symbol = s[i + 1]
        except IndexError:
            result = update_result_string(counter, letter, result)
        if next_symbol == letter:
            counter += 1
        if next_symbol != letter:
            result = update_result_string(counter, letter, result)
            counter = 1
    return result


def update_result_string(counter, letter, result):
    if counter == 1:
        result += letter
    else:
        result += f"{counter}{letter}"
    return result


def decompress(s):
    pass


if __name__ == "__main__":
    assert "abc" == compress("abc")
    assert "3ag6b2c4df" == compress("aaagbbbbbbccddddf")
    assert "3a6b2c3a4df" == compress("aaabbbbbbccaaaddddf")
    # compressed_str = compress(init_str)
    # assert init_str == decompress(compressed_str)
