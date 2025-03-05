import unittest
from stack import Stack


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(10)

    def test_push(self):
        self.stack.push(20)
        self.assertEqual(self.stack.top.data, 20)
        self.assertEqual(self.stack.height, 2)
        self.assertEqual(str(self.stack), "20-->10")

    def test_pop(self):
        self.stack.push(20)
        self.assertEqual(self.stack.pop().data, 20)
        self.assertEqual(self.stack.top.data, 10)
        self.assertEqual(self.stack.height, 1)
        self.assertEqual(str(self.stack), "10")


if __name__ == "__main__":
    unittest.main()
