from typing import Any, Generator


class Node:
    def __init__(self, data: int | str) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.data)


class DoublyLinkedList:
    def __init__(self, data: int | str) -> None:
        node: Node = Node(data)
        self.head: Node | None = node
        self.tail: Node | None = node
        self.length: int = 1

    def __iter__(self) -> Generator[Node | None, Any, None]:
        current: Node | None = self.head
        while current:
            yield current
            current = current.next

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        return "-->".join([str(node) for node in self])

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data: int | str) -> None:
        node: Node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self) -> Node | None:
        if self.length == 0:
            return None
        tmp: Node | None = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = tmp.prev
            self.tail.next = None
            tmp.prev = None
        self.length -= 1
        return tmp

    def prepend(self, data: int | str) -> None:
        node: Node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def pop_first(self) -> Node | None:
        if self.length == 0:
            return None
        head: Node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            head.next = None
        self.length -= 1
        return head

    def get(self, index: int) -> Node | None:
        if index not in range(self.length):
            raise IndexError("Index out of range")
        node: Node | None = self.head
        if index <= self.length // 2:
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length - index - 1):
                node = node.prev
        return node

    def set(self, index: int, data: int | str) -> None:
        node: Node = self.get(index)
        node.data = data

    def insert(self, index: int, data: int | str) -> None:
        if self.length == 0:
            self.head = Node(data)
            self.tail = Node(data)
        if index <= 0:
            return self.prepend(data)
        if index >= self.length:
            return self.append(data)
        else:
            next: Node = self.get(index)
            prev: Node | None = next.prev
            node: Node = Node(data)
            prev.next = node
            node.prev = prev
            node.next = next
            next.prev = node
        self.length += 1

    def remove(self, index: int) -> Node | None:
        if index not in range(self.length):
            raise ValueError(f"List has no element at index {index} ")
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        previous: Node = self.get(index - 1)
        node: Node = previous.next
        previous.next = node.next
        previous.next.prev = previous
        self.length -= 1
        return node


def main() -> None:
    dll: DoublyLinkedList = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    print(dll.pop_first())
    print(dll, len(dll))
    dll.append(4)
    print(dll, len(dll))
    print(dll.pop())
    print(dll, len(dll))
    print(dll.pop())
    print(dll, len(dll))
    dll.append(5)
    print(dll, len(dll))
    dll.prepend(6)
    print(dll, len(dll))
    dll.prepend(7)
    print(dll, len(dll))
    print(dll.get(0))
    print(dll.get(3))
    print(dll.get(1))
    print(dll.pop_first())
    print(dll, len(dll))
    dll.set(0, 1)
    dll.set(2, 188)
    print(dll, len(dll))

    dll.insert(2, 8)
    print(dll, len(dll))

    dll.insert(1, 2228)
    print(dll, len(dll))

    dll.insert(0, 11118)
    print(dll, len(dll))
    dll.insert(5, 11199918)
    print(dll, len(dll))


if __name__ == "__main__":
    main()
