def find_num_of_valid_words(words, puzzles):
    result = []

    for puzzle in puzzles:
        puzzle_set = set(puzzle)
        first_letter = puzzle[0]
        count = 0

        for word in words:
            word_set = set(word)
            if first_letter in word_set and word_set.issubset(puzzle_set):
                count += 1

        result.append(count)

    return result


if __name__ == "__main__":
    words = ["apple", "pleas", "please"]
    puzzles = ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]

    assert find_num_of_valid_words(words, puzzles) == [0, 1, 3, 2, 0]
