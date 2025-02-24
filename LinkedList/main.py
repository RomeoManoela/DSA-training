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
        current: Node = self.head
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
        tail: Node = self.tail
        previous: Node = self.head
        while previous.next.next:
            previous = previous.next
        self.tail = previous
        previous.next = None
        self.length -= 1
        return tail


def main() -> None:
    ll: LinkedList = LinkedList(2)
    print(ll, len(ll))
    ll.append(1)
    print(ll, len(ll))
    ll.append(2)
    print(ll, len(ll))
    ll.clear()
    ll.append(9)
    print(ll, len(ll))
    ll.append(12)
    print(ll, len(ll))
    ll.append(3)
    print(ll, len(ll))
    print(ll.pop())
    print(ll, len(ll))
    print(ll.pop())
    print(ll, len(ll))


if __name__ == "__main__":
    main()
