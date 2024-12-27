def word_break(s: str, word_dict: list[str]) -> bool:
    dp = [None] * len(s)

    def helper(start_position: int) -> int:
        if start_position == len(s):
            return True

        if dp[start_position] is None:
            answer = False
            for word in word_dict:
                end_position = start_position + len(word)
                if s[start_position:end_position] == word:
                    answer = helper(start_position=end_position)
                    if answer:
                        break
            dp[start_position] = answer

        return dp[start_position]

    return helper(start_position=0)


if __name__ == "__main__":
    assert word_break(s="leetcode", word_dict=["leet", "code"]) is True
    assert word_break(s="applepenapple", word_dict=["apple", "pen"]) is True
    assert (
        word_break(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"])
        is False
    )
