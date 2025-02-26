from LinkedList.main import LinkedList, Node


class MyLinkedList(LinkedList):

    def find_middle_node(self) -> Node:
        """Write a method to find and return the middle node in th
        Linked List WITHOUT using the length attribute"""
        slow: Node | None = self.head
        fast: Node | None = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def has_loop(self) -> bool:
        """Write a method called has_loop that is part of the linked list class.
        The method should be able to detect if there is a cycle or loop present
        in the linked list.
        The method should utilize Floyd's cycle-finding algorithm, also known as
        the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.
        """
        slow: Node | None = self.head
        fast: Node | None = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def remove_duplicate(self) -> None:
        """remove duplicate
        You are given a singly linked list that contains integer values, where some of
        these values may be duplicated.
        Your task is to implement a method called remove_duplicates() within the LinkedList
        class that removes all duplicate values from the list.
        Your method should not create a new list, but rather modify the existing list in-place,
        preserving the relative order of the nodes."""
        unique: set[int] = set()
        current: Node | None = self.head
        before: Node | None = self.head
        while current:
            if current.data not in unique:
                unique.add(current.data)
                before = current
            else:
                before.next = current.next
                self.length -= 1
            current = current.next

    def fin_kth(self, k: int) -> Node | None:
        """find_kth_from_end
        Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.
        For example, let's say you want to find the item that is 3 steps away from the end of the LL. To do this,
        you would start from the head of the LL and move through the links until you reach the item that is 3 steps
        away from the end.
        """
        slow: Node | None = self.head
        fast: Node | None = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow

    def reverse_between(self, first: int, second: int) -> None:
        """You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between
        within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in
         one pass and in-place."""
        a: Node = self.get(first)
        b: Node = self.get(second)
        a.data, b.data = b.data, a.data


def main():
    ll = MyLinkedList(1)
    ll.append(2)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    ll.append(3)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(6)
    ll.append(6)
    print(ll)
    print(ll.find_middle_node())
    print(ll.has_loop())
    ll.remove_duplicate()
    print(ll, ll.length)
    print(ll.fin_kth(3))
    ll.reverse_between(0, 2)
    print(ll)


if __name__ == "__main__":
    main()
