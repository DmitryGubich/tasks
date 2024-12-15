def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res = []

    def backtrack(combination, next_digits):
        if not next_digits:
            res.append(combination)
            return

        for letter in phone[next_digits[0]]:
            backtrack(combination + letter, next_digits[1:])

    backtrack("", digits)
    return res


if __name__ == "__main__":
    assert letter_combinations(digits="23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert letter_combinations(digits="2") == ["a", "b", "c"]
