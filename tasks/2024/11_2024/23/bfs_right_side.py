class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_right_side(root: TreeNode | None) -> list[int]:
    result = []
    if not root:
        return result
    cur_layer = [root]
    while cur_layer:
        result.append(cur_layer[-1].val)
        next_layer = []
        for node in cur_layer:
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        cur_layer = next_layer

    return result


if __name__ == "__main__":
    tn5 = TreeNode(val=5)
    tn4 = TreeNode(val=4)
    tn3 = TreeNode(val=3)
    tn2 = TreeNode(val=2, left=tn4, right=tn5)
    tn1 = TreeNode(val=1, left=tn2, right=tn3)
    assert bfs_right_side(tn1) == [1, 3, 5]
