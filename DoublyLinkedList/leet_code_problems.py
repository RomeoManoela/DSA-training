from main import DoublyLinkedList, Node


class MyLinkedList(DoublyLinkedList):
    def swap_first_last(self) -> None:
        """Swap the values of the first and last node"""
        if self.head is None:
            return
        self.head.data, self.tail.data = (self.tail.data, self.head.data)

    def reverse(self) -> None:
        """Create a new method called reverse that reverses the order of the
        nodes in the list, i.e., the first node becomes the last node, the
         second node becomes the second-to-last node, and so on."""
        if self.head is None:
            return
        current: Node | None = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def is_palindrome(self) -> bool:
        """Write a method to determine whether a given doubly linked list
         reads the same forwards and backwards.
        For example, if the list contains the values [1, 2, 3, 2, 1], then the
         method should return True, since the list is a palindrome.
        If the list contains the values [1, 2, 3, 4, 5], then the method should
         return False, since the list is not a palindrome."""
        forward: Node | None = self.head
        backward: Node | None = self.tail
        for _ in range(self.length // 2):
            print(forward, backward)
            if forward.data != backward.data:
                return False
            forward = forward.next
            backward = backward.prev
        return True
