import unittest

from main import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = LinkedList(1)

    def test_append(self) -> None:
        self.ll.append(2)
        self.assertEqual(str(self.ll), "1-->2")

    def test_pop(self) -> None:
        self.assertEqual(str(self.ll.pop()), "1")

    def test_prepend(self) -> None:
        self.ll.prepend(2)
        self.assertEqual(str(self.ll), "2-->1")
