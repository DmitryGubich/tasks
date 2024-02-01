def calculate_steps(steps: int) -> int:
    if steps == 0:
        return 1
    elif steps < 0:
        return 0

    return (
        calculate_steps(steps - 1)
        + calculate_steps(steps - 2)
        + calculate_steps(steps - 3)
    )


if __name__ == "__main__":
    assert calculate_steps(steps=3) == 4
    assert calculate_steps(steps=4) == 7
    assert calculate_steps(steps=5) == 13
