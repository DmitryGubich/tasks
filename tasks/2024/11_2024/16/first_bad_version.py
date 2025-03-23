def isBadVersion(n: int): ...


def first_bad_version(n: int) -> int:
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    assert first_bad_version(n=5) == 4
    assert first_bad_version(n=1) == 1
