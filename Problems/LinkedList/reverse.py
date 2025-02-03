from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node|None = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self, data: Any) -> None:
        node: Node = Node(data)
        self.head: Node|None = node
        self.tail: Node|None = node
        self.__length: int = 1

    def __iter__(self) -> None:
        node: Node|None = self.head
        while node:
            yield node
            node = node.next

    def __str__(self) -> str:
        return ' ->'.join([ str(data) for data in self])

    def __len__(self) -> int:
        return self.__length

    def append(self, data: Any) -> None:
        node: Node = Node(data)
        if self.__length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.__length += 1


def inverse(my_ll: LinkedList) -> bool:
    slow: Node|None = my_ll.head
    fast: Node|None = my_ll.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            print('There is a loop')
            return False
    before: Node|None = None
    current: Node|None = my_ll.head
    while current:
        after: Node|None = current.next
        current.next = before
        before = current
        current = after
    ll.head, ll.tail = ll.tail, ll.head
    return True




if __name__ == '__main__':
    ll: LinkedList = LinkedList(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    print(ll, len(ll))
    inverse(ll)
    print(ll, len(ll))

print([].__len__())
