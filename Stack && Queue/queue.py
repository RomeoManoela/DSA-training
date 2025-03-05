from typing import Generator, Any


class Node:
    def __init__(self, data: int | str) -> None:
        self.data: int | str = data
        self.next: Node | None = None

    def __str__(self) -> str:
        return str(self.data)


class MyQueue:
    def __init__(self, data: int | str) -> None:
        node: Node = Node(data)
        self.first: Node | None = node
        self.last: Node | None = node
        self.length: int = 1

    def __iter__(self) -> Generator[Node | None, Any, None]:
        current: Node | None = self.first
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        return "-->".join([str(data) for data in self])

    def enqueue(self, data: int | str) -> None:
        node: Node = Node(data)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self) -> Node | None:
        if self.length == 0:
            return None
        first: Node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = first.next
            first.next = None
        self.length -= 1
        return first
