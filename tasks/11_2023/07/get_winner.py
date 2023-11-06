def get_winner(arr: list[int], k: int) -> int:
    max_element = max(arr)
    winner = arr[0]
    streak = 0

    for i in range(1, len(arr)):
        if winner > arr[i]:
            streak += 1

        if arr[i] > winner:
            streak = 1
            winner = arr[i]

        if streak == k or winner == max_element:
            return winner


if __name__ == "__main__":
    assert get_winner(arr=[2, 1, 3, 5, 4, 3, 7], k=3) == 5
    assert get_winner(arr=[3, 2, 1], k=10) == 3
