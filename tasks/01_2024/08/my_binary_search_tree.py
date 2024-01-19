import json
from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value


class MyBinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return node

        current_root = self.root
        while True:
            if value < current_root.value:
                if not current_root.left:
                    current_root.left = node
                    return node
                current_root = current_root.left
            else:
                if not current_root.right:
                    current_root.right = node
                    return node
                current_root = current_root.right

    def lookup(self, value):
        current_root = self.root

        while True:
            if value < current_root.value:
                if not current_root.left:
                    return current_root.value == value
                current_root = current_root.left
            elif value > current_root.value:
                if not current_root.right:
                    return current_root.value == value
                current_root = current_root.right
            else:
                return True

    def height(self, root: Node):
        if root is None or root.left is None or root.right is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def is_symmetric(self):
        q = Queue()
        q.put((self.root, self.root))
        while q:
            l, r = q.get()
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.value == r.value:
                q.put((l.left, r.right))
                q.put((l.right, r.left))
            else:
                return False
        return True

    def BFS(self):
        result = []
        q = Queue()
        q.put(self.root)

        while not q.empty():
            current_node = q.get()
            result.append(current_node.value)
            if current_node.left:
                q.put(current_node.left)
            if current_node.right:
                q.put(current_node.right)
        return result

    def DFS_inorder(self, root: Node, values: list[int]):
        if root:
            self.DFS_inorder(root.left, values)
            values.append(root.value)
            self.DFS_inorder(root.right, values)

        return values

    def DFS_preorder(self, root: Node, values: list[int]):
        if root:
            values.append(root.value)
            self.DFS_preorder(root.left, values)
            self.DFS_preorder(root.right, values)

        return values

    def DFS_postorder(self, root: Node, values: list[int]):
        if root:
            self.DFS_postorder(root.left, values)
            self.DFS_postorder(root.right, values)
            values.append(root.value)

        return values

    def isValidBST(self) -> bool:
        values = self.DFS_inorder(self.root, [])

        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False

        return True


def traverse(node):
    return {
        "value": node.value,
        "left": None if not node.left else traverse(node.left),
        "right": None if not node.right else traverse(node.right),
    }


if __name__ == "__main__":
    tree = MyBinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print(
        json.dumps(
            traverse(tree.root),
            indent=4,
            default=str,
        )
    )
    print(tree.lookup(9))
    print(tree.lookup(6))
    print(tree.lookup(1))
    print(tree.lookup(170))
    print(tree.lookup(15))

    print(tree.lookup(14))
    print(tree.lookup(2))
    print(tree.lookup(39))
    print(tree.height(tree.root))
    print(tree.BFS())
    print(tree.DFS_inorder(tree.root, []))
    print(tree.DFS_preorder(tree.root, []))
    print(tree.DFS_postorder(tree.root, []))
    print(tree.isValidBST())
