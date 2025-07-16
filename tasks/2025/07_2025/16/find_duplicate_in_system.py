from collections import defaultdict


def find_duplicate(paths: list[str]) -> list[list[str]]:
    d = defaultdict(list)

    for s in paths:
        s = s.split(" ")  # parse the string: first component is
        path = s[0]  # the path; the other components are files

        for file in s[1:]:
            idx = file.index("(")  # Build a dict of files with key = file content
            d[file[idx:]].append(path + "/" + file[:idx])

            # return the dict values for keys w/ > 1 files
    return [v for _, v in d.items() if len(v) > 1]


if __name__ == "__main__":
    assert find_duplicate(
        [
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)",
        ]
    ) == [
        ["root/a/1.txt", "root/c/3.txt"],
        ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
    ]
