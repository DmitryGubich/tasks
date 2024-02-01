def int_to_roman(number: int) -> str:
    num_map = {
        1: "I",
        5: "V",
        4: "IV",
        10: "X",
        9: "IX",
        50: "L",
        40: "XL",
        100: "C",
        90: "XC",
        500: "D",
        400: "CD",
        1000: "M",
        900: "CM",
    }

    result = ""

    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while n <= number:
            result += num_map[n]
            number -= n
    return result


if __name__ == "__main__":
    assert int_to_roman(number=3) == "III"
    assert int_to_roman(number=58) == "LVIII"
    assert int_to_roman(number=1994) == "MCMXCIV"
