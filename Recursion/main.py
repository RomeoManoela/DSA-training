from BST.main import BST, Node


# solve factorial
def fact(x: int):
    if x == 2:
        return x
    return x * fact(x - 1)


# recursive binary search tree
def min_value(current_node: Node) -> int:
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.data


class MyBST(BST):
    def __r_contains(self, current_node: Node, value: int) -> bool | None:
        if current_node is None:
            return False
        if value == current_node.data:
            return True
        if value < current_node.data:
            return self.__r_contains(current_node.left, value)
        if value > current_node.data:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value: int) -> bool:
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node: Node, value: int) -> Node:
        if current_node is None:
            return Node(value)
        if value < current_node.data:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.data:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value: int) -> None:
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node: Node, value: int) -> Node | None:
        if current_node is None:
            return None
        if value < current_node.data:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.data:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                min_val: int = min_value(current_node.right)
                current_node.data = min_val
                current_node.right = self.__delete_node(current_node.right, min_val)

        return current_node

    def delete_node(self, value: int) -> None:
        self.__delete_node(self.root, value)


if __name__ == "__main__":
    print(fact(5))
    my_tree = MyBST(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print(my_tree.contain(21))
    print(my_tree.r_contains(27))
    my_tree.delete_node(27)
    print(my_tree.r_contains(27))
    my_tree.delete_node(21)
    print(my_tree.r_contains(21))
