from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_left_leaves(root: TreeNode | None) -> int:
    result = 0
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        if node:
            if node.left and not node.left.left and not node.left.right:
                result += node.left.val
            q.append(node.right)
            q.append(node.left)
    return result


if __name__ == "__main__":
    tn5 = TreeNode(val=7)
    tn4 = TreeNode(val=15)
    tn3 = TreeNode(val=20, left=tn4, right=tn5)
    tn2 = TreeNode(val=9)
    tn1 = TreeNode(val=3, left=tn2, right=tn3)
    assert sum_of_left_leaves(tn1) == 24
