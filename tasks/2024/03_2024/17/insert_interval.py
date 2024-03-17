def insert_interval(
    intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    result = []
    for interval in intervals:
        if interval[1] < new_interval[0]:
            result.append(interval)
        elif interval[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = interval
        else:
            new_interval[0] = min(interval[0], new_interval[0])
            new_interval[1] = max(interval[1], new_interval[1])
    result.append(new_interval)
    return result


if __name__ == "__main__":
    assert insert_interval(intervals=[[1, 3], [6, 9]], new_interval=[2, 5]) == [
        [1, 5],
        [6, 9],
    ]
    assert insert_interval(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval=[4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]
