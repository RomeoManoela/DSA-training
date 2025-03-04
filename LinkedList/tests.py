import unittest

from main import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = LinkedList(1)

    def test_append(self) -> None:
        self.ll.append(2)
        self.assertEqual(str(self.ll), "1-->2")
        self.assertEqual(len(self.ll), 2)

    def test_pop(self) -> None:
        self.assertEqual(str(self.ll.pop()), "1")
        self.assertEqual(len(self.ll), 0)

    def test_prepend(self) -> None:
        self.ll.prepend(2)
        self.assertEqual(str(self.ll), "2-->1")
        self.assertEqual(len(self.ll), 2)

    def test_pop_first(self) -> None:
        self.assertEqual(str(self.ll.pop_first()), "1")
        self.assertEqual(len(self.ll), 0)

    def test_insert(self) -> None:
        self.ll.insert(0, 10)
        self.assertEqual(str(self.ll), "10-->1")
        self.assertEqual(len(self.ll), 2)
