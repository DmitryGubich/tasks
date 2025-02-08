def are_almost_equal(s1: str, s2: str) -> bool:
    first_diff = 0
    second_diff = 0
    swaps = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            swaps += 1
            if swaps > 2:
                return False
            elif swaps == 1:
                first_diff = i
            else:
                second_diff = i

    return s1[first_diff] == s2[second_diff] and s1[second_diff] == s2[first_diff]


if __name__ == "__main__":
    assert are_almost_equal(s1="aa", s2="ac") is False
    assert are_almost_equal(s1="bank", s2="kanb") is True
    assert are_almost_equal(s1="attack", s2="defend") is False
