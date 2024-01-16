import json


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

    # def remove(self, value):
    #     if self.root is None:
    #         return False
    #     current_node = self.root
    #     parent_node = None
    #     while current_node:
    #         if value < current_node.value:
    #             parent_node = current_node
    #             current_node = current_node.left
    #         elif value > current_node.value:
    #             parent_node = current_node
    #             current_node = current_node.right
    #         else:
    #             if parent_node is None:
    #                 self.root = current_node.left
    #             else:
    #                 if current_node.value < parent_node.value:
    #                     parent_node.left = current_node.left
    #                 elif current_node.value > parent_node.value:
    #                     parent_node.right = current_node.right

    def height(self, root: Node):
        if root is None or root.left is None or root.right is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1


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
