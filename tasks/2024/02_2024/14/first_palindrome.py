def first_palindrome(words: list[str]) -> str:
    for w in words:
        if w == w[::-1]:
            return w
    return ""


if __name__ == "__main__":
    assert first_palindrome(words=["abc", "car", "ada", "racecar", "cool"]) == "ada"
    assert first_palindrome(words=["notapalindrome", "racecar"]) == "racecar"
