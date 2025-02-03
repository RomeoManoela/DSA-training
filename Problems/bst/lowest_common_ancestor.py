from typing import Any
from main import BinarySearchTree, Node


def lca(tree: BinarySearchTree) -> Any:
    left: Node|None = tree.root.left
    right: Node|None = tree.root.right