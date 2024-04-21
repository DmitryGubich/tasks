class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root: TreeNode | None) -> int:
    ans = 0

    def dfs(cur_node: TreeNode | None, num: int):
        if not cur_node.left and not cur_node.right:
            nonlocal ans
            ans += num * 10 + cur_node.val
            return

        if cur_node.left:
            dfs(cur_node.left, num * 10 + cur_node.val)

        if cur_node.right:
            dfs(cur_node.right, num * 10 + cur_node.val)

    dfs(root, 0)

    return ans


if __name__ == "__main__":
    tn5 = TreeNode(val=1)
    tn4 = TreeNode(val=5)
    tn3 = TreeNode(val=0)
    tn2 = TreeNode(val=9, left=tn4, right=tn5)
    tn1 = TreeNode(val=4, left=tn2, right=tn3)
    assert sum_numbers(tn1) == 1026
