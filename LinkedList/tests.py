import unittest
from main import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList(10)

    def test_append(self):
        self.ll.append(20)
        self.assertEqual(self.ll.tail.data, 20)
        self.assertEqual(len(self.ll), 2)

    def test_prepend(self):
        self.ll.prepend(5)
        self.assertEqual(self.ll.head.data, 5)
        self.assertEqual(len(self.ll), 2)

    def test_pop(self):
        self.ll.append(15)
        popped = self.ll.pop()
        self.assertEqual(popped.data, 15)
        self.assertEqual(self.ll.tail.data, 10)
        self.assertEqual(len(self.ll), 1)

    def test_pop_first(self):
        self.ll.append(20)
        popped = self.ll.pop_first()
        self.assertEqual(popped.data, 10)
        self.assertEqual(self.ll.head.data, 20)
        self.assertEqual(len(self.ll), 1)

    def test_get(self):
        self.ll.append(30)
        node = self.ll.get(1)
        self.assertEqual(node.data, 30)

    def test_set(self):
        self.ll.set(0, 50)
        self.assertEqual(self.ll.head.data, 50)

    def test_insert(self):
        self.ll.append(40)
        self.ll.insert(1, 30)
        self.assertEqual(self.ll.get(1).data, 30)
        self.assertEqual(len(self.ll), 3)

    def test_remove(self):
        self.ll.append(25)
        self.ll.append(35)
        removed = self.ll.remove(1)
        self.assertEqual(removed.data, 25)
        self.assertEqual(self.ll.get(1).data, 35)
        self.assertEqual(len(self.ll), 2)

    def test_reverse(self):
        self.ll.append(20)
        self.ll.append(30)
        self.ll.reverse()
        self.assertEqual(self.ll.head.data, 30)
        self.assertEqual(self.ll.tail.data, 10)

    def test_clear(self):
        self.ll.append(20)
        self.ll.clear()
        self.assertEqual(len(self.ll), 0)
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)

    def test_edge_cases(self):
        empty_list = LinkedList(0)
        empty_list.pop()
        self.assertIsNone(empty_list.head)
        self.assertIsNone(empty_list.tail)
        self.assertEqual(len(empty_list), 0)

        empty_list.append(5)
        self.assertEqual(empty_list.head.data, 5)
        self.assertEqual(empty_list.tail.data, 5)

        empty_list.prepend(2)
        self.assertEqual(empty_list.head.data, 2)
        self.assertEqual(empty_list.tail.data, 5)

        with self.assertRaises(IndexError):
            empty_list.get(10)

        with self.assertRaises(ValueError):
            empty_list.remove(10)


if __name__ == "__main__":
    unittest.main()
