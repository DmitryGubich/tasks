def compare_version(version1: str, version2: str) -> int:
    levels1 = version1.split(".")
    levels2 = version2.split(".")
    length = max(len(levels1), len(levels2))

    for i in range(length):
        v1 = int(levels1[i]) if i < len(levels1) else 0
        v2 = int(levels2[i]) if i < len(levels2) else 0
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1

    return 0


if __name__ == "__main__":
    assert compare_version(version1="1.01", version2="1.001") == 0
    assert compare_version(version1="1.0", version2="1.0.0") == 0
    assert compare_version(version1="1.0", version2="1.0.0") == 0
    assert compare_version(version1="0.1", version2="1.1") == -1
