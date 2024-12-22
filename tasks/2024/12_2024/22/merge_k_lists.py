import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, node)
    fake_node = ListNode(val=-1)
    head = fake_node
    while heap:
        next = heapq.heappop(heap)
        head.next = next
        head = head.next
        if head.next:
            heapq.heappush(heap, head.next)
    return fake_node.next


if __name__ == "__main__":
    last_node = ListNode(1)

    node_4 = ListNode(2)
    node_4.next = last_node

    node_3 = ListNode(3)
    node_3.next = node_4

    assert merge_k_lists(lists=[[1, 4, 5], [1, 3, 4], [2, 6]]) == [
        1,
        1,
        2,
        3,
        4,
        4,
        5,
        6,
    ]
    assert find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4
