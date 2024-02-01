from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    stack = []
    prev = None
    minimum_difference = float("inf")
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        minimum_difference = (
            min(root.val - prev.val, minimum_difference) if prev else minimum_difference
        )
        prev = root
        root = root
    return minimum_difference
