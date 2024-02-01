def count_and_say(n: int) -> str:
    result = ""
    n = str(n)
    for i in range(0, len(n), 2):
        a, b = n[i], n[i + 1]
        result += int(a) * b
    return result


if __name__ == "__main__":
    assert count_and_say(n=1211) == "21"
    assert count_and_say(n=2231) == "22111"
