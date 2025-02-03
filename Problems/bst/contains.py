from typing import Any
from main import BinarySearchTree


def contains(tree: BinarySearchTree, target: Any) -> bool:
    if tree.root is None:
        return False
    current = tree.root
    while current:
        if current.data == target:
            return True
        if target < current.data:
            current = current.left
        if target > current.data:
            current = current.right
    return False
