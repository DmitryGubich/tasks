def reverse_string(string: str) -> str:
    result = []
    for i in range(len(string) - 1, -1, -1):
        result.append(string[i])
    return "".join(result)


if __name__ == "__main__":
    assert reverse_string(string="Hi my name is Dima!") == "!amiD si eman ym iH"
