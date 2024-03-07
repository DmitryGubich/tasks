class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    if not head or not head.next:
        return False
    fast = head
    slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    last_node = ListNode(5)

    node_4 = ListNode(4)
    node_4.next = last_node

    node_3 = ListNode(3)
    node_2 = ListNode(2)

    node_3.next = node_2
    node_2.next = node_3

    node = ListNode(1)
    node.next = node_2

    assert has_cycle(head=node) is True
