class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root: TreeNode | None) -> list[str]:
    result = []

    def solve(node, s):
        s += str(node.val)
        if node.left:
            solve(node.left, s + "->")
        if node.right:
            solve(node.right, s + "->")
        if not node.left and not node.right:
            result.append(s)

    solve(root, "")
    return result


if __name__ == "__main__":
    tn5 = TreeNode(val=5)
    tn4 = TreeNode(val=4)
    tn3 = TreeNode(val=3)
    tn2 = TreeNode(val=2, left=tn4, right=tn5)
    tn1 = TreeNode(val=1, left=tn2, right=tn3)
    assert binary_tree_paths(tn1) == ["1->2->4", "1->2->5", "1->3"]
