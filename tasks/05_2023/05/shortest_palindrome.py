def shortest_palindrome(string: str) -> str:
    reverse = string[::-1]
    for i in range(len(reverse)):
        if string.startswith(reverse[i:]):
            return reverse[:i] + string
    return reverse + string


if __name__ == "__main__":
    assert shortest_palindrome(string="abc") == "cbabc"
    assert shortest_palindrome(string="abcd") == "dcbabcd"
