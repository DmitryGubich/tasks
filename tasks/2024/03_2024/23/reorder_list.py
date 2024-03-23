# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: ListNode | None) -> ListNode | None:
    list_vals = []
    curr = head
    while curr:
        list_vals.append(curr.val)
        curr = curr.next

    curr = head
    count = 1
    while curr:
        if count % 2 == 0:
            curr.val = list_vals.pop()
        else:
            curr.val = list_vals.pop(0)
        count += 1
        curr = curr.next
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
    last_node = ListNode(3)

    node_4 = ListNode(4)
    node_4.next = last_node

    node_3 = ListNode(2)
    node_3.next = node_4

    node_2 = ListNode(5)
    node_2.next = node_3

    new_node = ListNode(1)
    new_node.next = node_2

    assert reorder_list(node) is new_node
