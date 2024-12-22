import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


def values(head):
    cur = head
    result = [head.val]
    while cur.next:
        cur = cur.next
        result.append(cur.val)
    return result


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
    last_node = ListNode(4)
    first_list = ListNode(2)
    first_list.next = last_node

    last_node_2 = ListNode(3)
    second_list = ListNode(1)
    second_list.next = last_node_2

    four = ListNode(4)
    third = ListNode(3)
    second = ListNode(2)
    result = ListNode(1)
    third.next = four
    second.next = third
    result.next = second

    assert values(merge_k_lists(lists=[first_list, second_list])) == values(result)
