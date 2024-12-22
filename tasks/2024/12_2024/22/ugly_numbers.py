import heapq


def nth_ugly_number(n: int) -> int:
    heap = [1]
    number = 0
    for i in range(n):
        number = heapq.heappop(heap)
        while heap and number == heap[0]:
            number = heapq.heappop(heap)
        heapq.heappush(heap, number * 2)
        heapq.heappush(heap, number * 3)
        heapq.heappush(heap, number * 5)
    return number


if __name__ == "__main__":
    assert nth_ugly_number(n=10) == 12
    assert nth_ugly_number(n=1) == 1
