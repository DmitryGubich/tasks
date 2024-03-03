class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def values(head):
    cur = head
    result = [head.val]
    while cur.next:
        cur = cur.next
        result.append(cur.val)
    return result


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    fast = head
    slow = head

    for _ in range(n):
        fast = fast.next

    if fast is None:
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head


if __name__ == "__main__":
    last_node = ListNode(5)

    node_4 = ListNode(4)
    node_4.next = last_node

    node_3 = ListNode(3)
    node_3.next = node_4

    node_2 = ListNode(2)
    node_2.next = node_3

    node = ListNode(1)
    node.next = node_2

    # expected result
    last_node = ListNode(5)

    node_3 = ListNode(3)
    node_3.next = last_node

    node_2 = ListNode(2)
    node_2.next = node_3

    result_node = ListNode(1)
    result_node.next = node_2

    assert values(remove_nth_from_end(head=node, n=2)) == values(result_node)
