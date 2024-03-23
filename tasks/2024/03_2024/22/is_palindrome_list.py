# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode | None) -> bool:
    list_vals = []
    while head:
        list_vals.append(head.val)
        head = head.next

    left = 0
    right = len(list_vals) - 1
    while left < right:
        if list_vals[left] != list_vals[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    last_node = ListNode(1)

    node_4 = ListNode(2)
    node_4.next = last_node

    node_3 = ListNode(3)
    node_3.next = node_4

    node_2 = ListNode(2)
    node_2.next = node_3

    node = ListNode(1)
    node.next = node_2

    assert is_palindrome(node) is True
