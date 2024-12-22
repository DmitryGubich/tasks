import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    assert find_kth_largest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
    assert find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
