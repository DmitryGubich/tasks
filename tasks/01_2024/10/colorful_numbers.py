def colorful_numbers(s: str) -> bool:
    hashset = set()

    for i in range(1, len(s)):
        for j in range(0, len(s) - i + 1):
            sub = str(s)[j : j + i]

            product = 1
            for element in sub:
                product *= int(element)

            if product in hashset:
                return False
            else:
                hashset.add(product)
    return True


if __name__ == "__main__":
    assert colorful_numbers(s="3245") is True
    assert colorful_numbers(s="326") is False
