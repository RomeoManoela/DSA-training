from main import BinarySearchTree
from contains import contains
from smallerValue import smaller_value


def main():
    my_tree = BinarySearchTree(12)
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(7)
    my_tree.insert(1)
    my_tree.insert(2)
    my_tree.insert(6)
    my_tree.insert(8)
    print(contains(my_tree, 9))
    print(smaller_value(my_tree))

if __name__ == '__main__':
    main()