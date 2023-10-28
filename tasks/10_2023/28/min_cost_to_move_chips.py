def min_cost_to_move_chips(position: list[int]) -> int:
    odd, even = 0, 0
    for i in position:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return min(even, odd)


if __name__ == "__main__":
    assert min_cost_to_move_chips(position=[1, 2, 3]) == 1
    assert min_cost_to_move_chips(position=[2, 2, 2, 3, 3]) == 2
