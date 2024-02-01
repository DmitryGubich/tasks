def backspace_compare(s: str, t: str) -> bool:
    def generate_str_stack(string: str) -> list:
        result = []
        for i in string:
            if i != "#":
                result.append(i)
            elif result:
                result.pop()
        return result

    return generate_str_stack(s) == generate_str_stack(t)


if __name__ == "__main__":
    assert backspace_compare(s="y#fo##f", t="y#f#o##f") is True
    assert backspace_compare(s="a##c", t="#a#c") is True
    assert backspace_compare(s="ab##", t="c#d#") is True
    assert backspace_compare(s="a#c", t="b") is False
