def merge_alternately(word1: str, word2: str) -> str:
    result = ""
    n = min(len(word1), len(word2))
    for i in range(n):
        result += word1[i] + word2[i]
    result += word1[n:] + word2[n:]
    return result


if __name__ == "__main__":
    assert merge_alternately(word1="abc", word2="pqr") == "apbqcr"
    assert merge_alternately(word1="ab", word2="pqrs") == "apbqrs"
