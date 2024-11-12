def longest_mountain(arr: list[int]) -> int:
    i = ans = 0
    while i < len(arr):
        base = i
        # walk up
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1

        # check if peak is valid
        if i == base:
            i += 1
            continue
        peak = i

        # walk down
        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            i += 1

        # check if end is valid
        if i == peak:
            i += 1
            continue

        # update answer
        ans = max(ans, i - base + 1)

    return ans


if __name__ == "__main__":
    assert longest_mountain(arr=[2, 1, 4, 7, 3, 2, 5]) == 5
    assert longest_mountain(arr=[2, 2, 2]) == 0
