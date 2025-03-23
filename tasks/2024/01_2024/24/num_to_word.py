def number_to_words(num: int) -> str:
    names = {
        1_000: "Thousand",
        100: "Hundred",
        90: "Ninety",
        80: "Eighty",
        70: "Seventy",
        60: "Sixty",
        50: "Fifty",
        40: "Forty",
        30: "Thirty",
        20: "Twenty",
        19: "Nineteen",
        18: "Eighteen",
        17: "Seventeen",
        16: "Sixteen",
        15: "Fifteen",
        14: "Fourteen",
        13: "Thirteen",
        12: "Twelve",
        11: "Eleven",
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
        0: "Zero",
    }

    if num <= 20:
        return names[num]

    ans = []

    thousands = num // 1_000

    if thousands:
        ans.append(number_to_words(thousands))
        ans.append(names[1_000])
        num -= thousands * 1_000

    hundreds = num // 100

    if hundreds:
        ans.append(number_to_words(hundreds))
        ans.append(names[100])
        num -= hundreds * 100

    tens = num // 10

    if tens >= 2:
        ans.append(names[tens * 10])
        num -= tens * 10

    if num:
        ans.append(names[num])

    return " ".join(ans)


if __name__ == "__main__":
    assert number_to_words(num=1957) == "One Thousand Nine Hundred Fifty Seven"
    assert number_to_words(num=24839) == "Twenty Four Thousand Eight Hundred Thirty Nine"
