from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.left: Node| None = None
        self.right: Node| None = None

    def __str__(self) -> str:
        return str(self.data)


class BinarySearchTree:
    def __init__(self, data: Any=None) -> None:
        self.root: Node| None = Node(data) if data is not None else None

    def insert(self, data: Any) -> bool:
        if self.root is None:
            self.root = Node(data)
            return True
        current = self.root
        while current:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return True
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return True
                current = current.right
            else:
                return False

    def contains(self, data: Any) -> bool:
        if self.root is None:
            return False
        current = self.root
        while current:
            if data < current.data:
                if current.left is None:
                    return False
                current = current.left
            elif data > current.data:
                if current.right is None:
                    return False
                current = current.right
            else:
                return True


bst: BinarySearchTree = BinarySearchTree(3)
bst.insert(1)
bst.insert(2)
bst.insert(40)
print(bst.root.right)
print(bst.root.left.right)
print(bst.contains(40))