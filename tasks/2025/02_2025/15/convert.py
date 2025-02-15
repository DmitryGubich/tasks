def convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    row_arr = [""] * num_rows
    row_idx = 0
    up = True

    for ch in s:
        row_arr[row_idx] += ch
        if row_idx == num_rows - 1:
            up = False
        elif row_idx == 0:
            up = True

        if up:
            row_idx += 1
        else:
            row_idx -= 1

    return "".join(row_arr)


if __name__ == "__main__":
    assert convert(s="PAYPALISHIRING", num_rows=3) == "PAHNAPLSIIGYIR"
    assert convert(s="PAYPALISHIRING", num_rows=4) == "PINALSIGYAHRPI"
