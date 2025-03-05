from typing import Any, Generator


class Node:
    def __init__(self, data: int | str) -> None:
        self.data: int | str = data
        self.next: Node | None = None

    def __str__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self, data: int | str) -> None:
        self.top: Node | None = Node(data)
        self.height: int = 1

    def __iter__(self) -> Generator[Node | None, Any, None]:
        current: Node | None = self.top
        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        return "-->".join([str(data) for data in self])

    def push(self, data: int | str) -> None:
        node: Node = Node(data)
        if self.height == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.height += 1

    def pop(self) -> Node | None:
        if self.height == 0:
            return None
        top: Node = self.top
        self.top = top.next
        top.next = None
        self.height -= 1
        return top
