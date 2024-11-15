def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


if __name__ == "__main__":
    assert merge_intervals(intervals=[[2, 6], [1, 3], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert merge_intervals(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
