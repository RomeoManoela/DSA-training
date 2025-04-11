from LinkedList.main import LinkedList, Node


class MyLL(LinkedList):

    def bubble_sort(self):
        if self.length < 2:
            return
        sorted_until = None
        while sorted_until != self.head.next:
            current = self.head
            while current.next != sorted_until:
                after = current.next
                if current.data > after.data:
                    current.data, after.data = after.data, current.data
                current = current.next
            sorted_until = current

    def selection_sort(self):
        if self.length < 2:
            return
        current = self.head
        while current.next is not None:
            min_node = current
            tmp = current.next
            while tmp:
                if tmp.data < min_node.data:
                    min_node = tmp
                tmp = tmp.next
            if min_node != current:
                current.data, min_node.data = min_node.data, current.data
            current = current.next

if __name__ == "__main__":
    ll = MyLL(2)
    ll.append(1)
    ll.append(4)
    ll.append(0)
    ll.append(3)
    ll.append(0)
    ll.append(5)
    ll.append(4)
    ll.append(3)
    print(ll.head)
    print(ll.tail)
    print(ll)
    ll.selection_sort()
    print(ll)
    print(ll.head)
    print(ll.tail)
