def number_of_provinces(cities: list[list[int]]) -> int:
    def dfs(city):
        for neighbor, connected in enumerate(cities[city]):
            if connected == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    result = 0
    visited = set()
    for city in range(len(cities)):
        if city not in visited:
            visited.add(city)
            dfs(city)
            result += 1

    return result


if __name__ == "__main__":
    assert number_of_provinces(cities=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert number_of_provinces(cities=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
