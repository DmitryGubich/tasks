def decompress_string(data: str) -> str:
    result = ""
    for i in range(len(data)):
        symbol = data[i]
        if symbol.isnumeric():
            result += data[i - 1] * (int(symbol) - 1)
        else:
            result += symbol
    return result


if __name__ == "__main__":
    assert decompress_string("abc") == "abc"
    assert decompress_string("a3gb6c2d4f") == "aaagbbbbbbccddddf"
    assert decompress_string("a3b6c2a3d4f") == "aaabbbbbbccaaaddddf"
