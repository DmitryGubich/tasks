def can_form_palindrome(s: str) -> bool:
    letters = {}
    for char in s:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    odd_count = 0
    for i in letters.values():
        if i % 2 != 0:
            odd_count += 1

    return odd_count <= 1


if __name__ == "__main__":
    assert can_form_palindrome(s="cciiv") is True
    assert can_form_palindrome(s="hello") is False
