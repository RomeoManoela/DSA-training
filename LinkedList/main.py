class Node:
    def __init__(self, data: str | int) -> None:
        self.data: str | int = data
        self.next: Node | None = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self, data: str | int) -> None:
        node: Node = Node(data)
        self.head: Node = node
        self.tail: Node = node
        self.length: int = 1

    def __iter__(self):
        current: Node | None = self.head
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        return "-->".join([str(data) for data in self])

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def append(self, data: str | int) -> None:
        node: Node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self) -> Node | None:
        if self.length == 0:
            return None
        current: Node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            previous: Node = self.head
            while previous.next:
                previous = current
                current = current.next
            self.tail = previous
            previous.next = None
        self.length -= 1
        return current

    def prepend(self, data: str | int) -> None:
        node: Node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop_first(self) -> Node | None:
        if self.length == 0:
            return None
        head: Node = self.head
        self.head = head.next
        head.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return head

    def get(self, index: int) -> Node | None:
        if index not in range(self.length):
            raise IndexError("out of range")
        current: Node = self.head
        for _ in range(index):
            current = current.next
        return current

    def set(self, index: int, data: int | str) -> None:
        self.get(index).data = data

    def insert(self, index: int, data: int | str) -> None:
        if index <= 0:
            return self.prepend(data)
        if index >= self.length:
            return self.append(data)
        previous: Node = self.get(index - 1)
        node: Node = Node(data)
        node.next = previous.next
        previous.next = node
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
        self.length -= 1
        return node

    def reverse(self) -> None:
        current: Node = self.head
        before: Node | None = None
        while current:
            after: Node | None = current.next
            current.next = before
            before = current
            current = after
        self.head, self.tail = self.tail, self.head


def main() -> None:
    ll: LinkedList = LinkedList(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll, len(ll))
    print(ll.pop())
    print(ll, len(ll))
    ll.append(51)
    ll.prepend(100)
    print(ll, len(ll))
    ll.set(0, 111)
    print(ll, len(ll))
    ll.set(3, 11111111111)
    print(ll, len(ll))
    ll.insert(3, 222)
    print(ll, len(ll))
    ll.insert(0, 333)
    print(ll, len(ll))
    ll.insert(35555, 444)
    print(ll, len(ll))
    ll.insert(4, 555)
    print(ll, len(ll))
    ll.insert(-4, 666)
    print(ll, len(ll))
    print(ll.remove(4))
    print(ll, len(ll))
    print(ll.remove(6))
    print(ll, len(ll))
    print(ll.remove(0))
    print(ll, len(ll))
    ll.reverse()
    print(ll, len(ll))


if __name__ == "__main__":
    main()
