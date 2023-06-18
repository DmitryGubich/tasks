def process_list(list_of_words=None):
    if not list_of_words:
        return []
    result_map = {
        word: []
        for word in list_of_words
        if not (type(word) == int or type(word) == float)
    }
    for word in list_of_words:
        for key in result_map.keys():
            if sorted(list(word)) == sorted(list(key)):
                result_map[key].append(word)
    result = []
    for r in [k for k in result_map.values()]:
        if r not in result:
            result.append(r)
    return result


if __name__ == "__main__":
    assert process_list(
        [
            "cat",
            "tac",
            "some",
            "arc",
            "car",
            "arm",
            "assert",
            "asters",
            "stares",
            "catt",
        ]
    ) == [
        ["cat", "tac"],
        ["some"],
        ["arc", "car"],
        ["arm"],
        ["assert", "asters", "stares"],
        ["catt"],
    ]
