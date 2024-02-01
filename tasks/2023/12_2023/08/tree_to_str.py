class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_str(root: TreeNode | None) -> str:
    if root is None:
        return ""

    result = str(root.val)

    if root.left is None and root.right is None:
        result += ""

    if root.left:
        result += "({})".format(tree_to_str(root.left))

    if root.left is None and root.right:
        result += "()"

    if root.right:
        result += "({})".format(tree_to_str(root.right))

    return result


if __name__ == "__main__":
    tn4 = TreeNode(val=4)
    tn3 = TreeNode(val=3)
    tn2 = TreeNode(val=2, left=tn4)
    tn1 = TreeNode(val=1, left=tn2, right=tn3)

    assert tree_to_str(root=tn1) == "1(2(4))(3)"

    tn4 = TreeNode(val=4)
    tn3 = TreeNode(val=3)
    tn2 = TreeNode(val=2, right=tn4)
    tn1 = TreeNode(val=1, left=tn2, right=tn3)

    assert tree_to_str(root=tn1) == "1(2()(4))(3)"
