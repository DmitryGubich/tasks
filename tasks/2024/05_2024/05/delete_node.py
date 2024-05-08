class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


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

    delete_node(node=node_3)

    assert node
