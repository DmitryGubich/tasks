def best_workers(teams: list[str]) -> int:
    result = {}
    for team in teams:
        key = "".join(sorted(team))
        result[key] = result.get(key, 0) + 1
    return max(result.values())


if __name__ == "__main__":
    assert best_workers(teams=["M V G", "V M G", "I D V", "A D V"]) == 2
    assert best_workers(teams=["M V G", "V M G", "G M V", "A D V"]) == 3
