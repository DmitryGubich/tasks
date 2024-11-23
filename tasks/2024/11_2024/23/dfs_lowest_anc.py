class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root

    l = lowest_common_ancestor(root.left, p, q)
    r = lowest_common_ancestor(root.right, p, q)

    if l and r:
        return root
    return l or r


if __name__ == "__main__":
    tn5 = TreeNode(val=5)
    tn4 = TreeNode(val=4)
    tn3 = TreeNode(val=3)
    tn2 = TreeNode(val=2, left=tn4, right=tn5)
    tn1 = TreeNode(val=1, left=tn2, right=tn3)
    assert lowest_common_ancestor(tn1, tn4, tn5) == tn2
