class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self) -> str:
        return str(self.data)


# Binary search tree
class BST:
    def __init__(self, data: int) -> None:
        self.root: Node | None = Node(data)

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
            return
        current: Node | None = self.root
        while 1:
            if data == current.data:
                return
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                current = current.left
            if data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right

    def contain(self, item: int) -> bool:
        if self.root is None:
            return False
        current: Node | None = self.root
        while current is not None:
            if item == current.data:
                return True
            elif item < current.data:
                current = current.left
            else:
                current = current.right
        return False
