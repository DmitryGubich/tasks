def count_num_ways(s: str, k: int) -> int:
    result = 0

    for i in range(len(s) - k + 1):
        substring = s[i : i + k]
        if substring > substring[::-1]:
            result += 1

    return result


if __name__ == "__main__":
    assert count_num_ways(s="amazon", k=3) == 1
    assert count_num_ways(s="ababa", k=2) == 2
    assert count_num_ways(s="aaaa", k=4) == 0
