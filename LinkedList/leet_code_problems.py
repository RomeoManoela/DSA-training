from LinkedList.main import LinkedList, Node


class MyLinkedList(LinkedList):
    # Write a method to find and return the middle node in th
    # Linked List WITHOUT using the length attribute
    def find_middle_node(self) -> Node:
        slow: Node | None = self.head
        fast: Node | None = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    # Write a method called has_loop that is part of the linked list class.
    # The method should be able to detect if there is a cycle or loop present
    # in the linked list.
    # The method should utilize Floyd's cycle-finding algorithm, also known as
    # the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.
    def has_loop(self) -> bool:
        slow: Node | None = self.head
        fast: Node | None = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


def main():
    ll = MyLinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print(ll)
    print(ll.find_middle_node())
    print(ll.has_loop())


if __name__ == "__main__":
    main()
