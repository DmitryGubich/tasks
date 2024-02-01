def binary_string(s: str) -> int:
    left = counter = answer = 0

    for right in range(len(s)):
        if s[right] == "0":
            counter += 1
        while counter > 1:
            if s[left] == "0":
                counter -= 1
            left += 1
        answer = max(answer, right - left + 1)

    return answer


if __name__ == "__main__":
    assert binary_string(s="1101100111") == 5
