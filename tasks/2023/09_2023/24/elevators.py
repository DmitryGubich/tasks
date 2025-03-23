def elevators(floors: list[list[int, int]]) -> int:
    result = 1
    while floors:
        first_floor = min(floor[0] for floor in floors)
        next_floor = min(floor[1] for floor in floors if floor[0] == first_floor)
        floors = [
            floor
            for floor in floors
            if floor[0] != first_floor or floor[0] == floor[1] == first_floor
        ]
        if [first_floor, next_floor] in floors:
            floors.remove([first_floor, next_floor])
        return result + elevators(floors)
    return result


if __name__ == "__main__":
    assert elevators(floors=[[2, 6], [5, 6], [2, 5], [2, 2], [6, 8], [2, 2], [0, 2]]) == 6
    assert (
        elevators(
            floors=[
                [2, 6],
                [5, 6],
                [2, 5],
                [2, 2],
                [6, 8],
                [2, 2],
                [0, 2],
                [2, 3],
                [3, 5],
            ]
        )
        == 7
    )
