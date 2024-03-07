class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: ListNode | None) -> ListNode:
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


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

    assert middle_node(head=node) == node_3
