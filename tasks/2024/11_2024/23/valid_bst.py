class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def valid_bst(root: TreeNode | None) -> bool:
    values = []

    def get_values(node: TreeNode):
        if node.left:
            get_values(node.left)
        values.append(node.val)
        if node.right:
            get_values(node.right)

    get_values(root)

    for i in range(1, len(values)):
        if values[i - 1] >= values[i]:
            return False

    return True


if __name__ == "__main__":
    tn5 = TreeNode(val=5)
    tn4 = TreeNode(val=4)
    tn3 = TreeNode(val=3)
    tn2 = TreeNode(val=2, left=tn4, right=tn5)
    tn1 = TreeNode(val=1, left=tn2, right=tn3)
    assert valid_bst(tn1) is False
