def buddy_strings(s: str, goal: str) -> bool:
    diffs = [(a, b) for a, b in zip(s, goal) if a != b]
    return len(diffs) == 2 and diffs[0] == diffs[1][::-1]


if __name__ == "__main__":
    assert buddy_strings(s="ab", goal="ba") is True
