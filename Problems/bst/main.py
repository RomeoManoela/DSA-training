from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.left: Node|None = None
        self.right: Node|None = None

    def __str__(self) -> str:
        return str(self.data)


class BinarySearchTree:
    def __init__(self, data: Any) -> None:
        self.root: Node|None = Node(data)

    def insert(self, data: Any) -> None:
        node: Any = Node(data)
        if self.root is None:
            self.root = node
            return
        current: Node|None = self.root
        while current:
            if current.data == node.data:
                return
            if current.data > node.data:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right


if __name__ == '__main__':
    tree: BinarySearchTree = BinarySearchTree(5)
    tree.insert(5)
    tree.insert(1)
    tree.insert(2)
    tree.insert(7)
    tree.insert(0)
    tree.insert(6)
    print(tree.root.right.left)