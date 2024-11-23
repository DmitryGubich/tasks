class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    max_left = depth(root.left)
    max_right = depth(root.right)

    return max(max_left, max_right) + 1


if __name__ == "__main__":
    tn5 = TreeNode(val=1)
    tn4 = TreeNode(val=5)
    tn3 = TreeNode(val=0)
    tn2 = TreeNode(val=9, left=tn4, right=tn5)
    tn1 = TreeNode(val=4, left=tn2, right=tn3)
    assert depth(tn1) == 3
