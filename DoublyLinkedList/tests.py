import unittest
from main import DoublyLinkedList


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList(10)

    def test_append(self):
        self.dll.append(20)
        self.assertEqual(self.dll.tail.data, 20)
        self.assertEqual(self.dll.tail.prev.data, 10)
        self.assertEqual(len(self.dll), 2)

    def test_prepend(self):
        self.dll.prepend(5)
        self.assertEqual(self.dll.head.data, 5)
        self.assertEqual(self.dll.head.next.data, 10)
        self.assertEqual(len(self.dll), 2)

    def test_pop(self):
        self.dll.append(15)
        popped = self.dll.pop()
        self.assertEqual(popped.data, 15)
        self.assertEqual(self.dll.tail.data, 10)
        self.assertIsNone(self.dll.tail.next)
        self.assertEqual(len(self.dll), 1)

    def test_pop_first(self):
        self.dll.append(20)
        popped = self.dll.pop_first()
        self.assertEqual(popped.data, 10)
        self.assertEqual(self.dll.head.data, 20)
        self.assertIsNone(self.dll.head.prev)
        self.assertEqual(len(self.dll), 1)

    def test_get(self):
        self.dll.append(30)
        node = self.dll.get(1)
        self.assertEqual(node.data, 30)
        self.assertEqual(node.prev.data, 10)

    def test_set(self):
        self.dll.set(0, 50)
        self.assertEqual(self.dll.head.data, 50)

    def test_insert(self):
        self.dll.append(40)
        self.dll.insert(1, 30)
        self.assertEqual(self.dll.get(1).data, 30)
        self.assertEqual(self.dll.get(1).prev.data, 10)
        self.assertEqual(self.dll.get(1).next.data, 40)
        self.assertEqual(len(self.dll), 3)

    def test_remove(self):
        self.dll.append(25)
        self.dll.append(35)
        removed = self.dll.remove(1)
        self.assertEqual(removed.data, 25)
        self.assertEqual(self.dll.get(1).data, 35)
        self.assertEqual(self.dll.get(1).prev.data, 10)
        self.assertEqual(len(self.dll), 2)

    def test_clear(self):
        self.dll.append(20)
        self.dll.clear()
        self.assertEqual(len(self.dll), 0)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)

    def test_edge_cases(self):
        empty_list = DoublyLinkedList(0)
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
