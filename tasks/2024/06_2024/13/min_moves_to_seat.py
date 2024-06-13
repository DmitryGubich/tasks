def min_moves_to_seat(seats: list[int], students: list[int]) -> int:
    seats.sort()
    students.sort()
    moves = 0

    for i in range(len(seats)):
        moves += abs(seats[i] - students[i])

    return moves


if __name__ == "__main__":
    assert min_moves_to_seat(seats=[3, 1, 5], students=[2, 7, 4]) == 4
    assert min_moves_to_seat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]) == 7
