def roman_to_int(s: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    i = 0
    num = 0
    while i < len(s):
        if s[i : i + 2] in roman:
            num += roman[s[i : i + 2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num


if __name__ == "__main__":
    assert roman_to_int(s="III") == 3
    assert roman_to_int(s="LVIII") == 58
    assert roman_to_int(s="MCMXCIV") == 1994
