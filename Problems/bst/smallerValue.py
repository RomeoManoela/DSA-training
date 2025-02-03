from main import BinarySearchTree, Node

def smaller_value(bst: BinarySearchTree) -> Node :
    current = bst.root
    while current.left:
        current = current.left
    return current

