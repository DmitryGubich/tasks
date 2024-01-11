def pdf_viewer(h: list, word: str) -> int:
    max_elem = float("-inf")
    for letter in word:
        cur_elem = h[ord(letter) - 97]
        if cur_elem > max_elem:
            max_elem = cur_elem
    return max_elem * len(word)


if __name__ == "__main__":
    assert (
        pdf_viewer(
            h=[
                1,
                3,
                1,
                3,
                1,
                4,
                1,
                3,
                2,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                7,
            ],
            word="zaba",
        )
        == 28
    )
