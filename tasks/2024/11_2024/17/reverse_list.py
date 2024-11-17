# Definition for singly-linked list.
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


def reverse_list(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


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
    last_node = ListNode(1)

    node_4 = ListNode(2)
    node_4.next = last_node

    node_3 = ListNode(3)
    node_3.next = node_4

    node_2 = ListNode(4)
    node_2.next = node_3

    result_node = ListNode(5)
    result_node.next = node_2

    assert values(reverse_list(head=node)) == values(result_node)
