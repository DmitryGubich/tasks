def capitalize_title(title: str) -> str:
    result = []
    words = title.split()
    for word in words:
        if len(word) <= 2:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return " ".join(result)


if __name__ == "__main__":
    assert capitalize_title(title="capiTalIze tHe titLe") == "Capitalize The Title"
    assert capitalize_title(title="First leTTeR of EACH Word") == "First Letter of Each Word"
