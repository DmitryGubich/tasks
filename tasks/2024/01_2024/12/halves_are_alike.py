def halves_are_alike(s: str) -> bool:
    vowels = set("aeiouAEIOU")
    mid = len(s) // 2
    a, b = s[:mid], s[mid:]
    return len([i for i in a if i in vowels]) == len([i for i in b if i in vowels])


if __name__ == "__main__":
    assert halves_are_alike(s="book") is True
    assert halves_are_alike(s="textbook") is False
