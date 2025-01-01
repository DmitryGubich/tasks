def is_interleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    def helper(s1_start: int, s2_start: int) -> int:
        if s1_start == len(s1) and s2_start == len(s2):
            return True

        answer = False
        if dp[s1_start][s2_start] is None:
            if s1_start < len(s1) and s1[s1_start] == s3[s1_start + s2_start]:
                answer = answer or helper(s1_start=s1_start + 1, s2_start=s2_start)
            if s2_start < len(s2) and s2[s2_start] == s3[s1_start + s2_start]:
                answer = answer or helper(s1_start=s1_start, s2_start=s2_start + 1)
            dp[s1_start][s2_start] = answer

        return dp[s1_start][s2_start]

    return helper(s1_start=0, s2_start=0)


if __name__ == "__main__":
    assert is_interleave(s1="aabc", s2="abad", s3="aabcabad") is True
    assert is_interleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") is True
    assert is_interleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") is False
