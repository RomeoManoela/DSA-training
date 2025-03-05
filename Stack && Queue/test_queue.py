import unittest
from .queue import MyQueue


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = MyQueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(str(queue), "1-->2-->3")
        self.assertEqual(queue.length, 3)

    def test_dequeue(self):
        queue = MyQueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        dequeued = queue.dequeue()
        self.assertEqual(dequeued.data, 1)
        self.assertEqual(str(queue), "2-->3")
        self.assertEqual(queue.length, 2)

    def test_dequeue_empty(self):
        queue = MyQueue(1)
        queue.dequeue()  # Suppression du seul élément
        self.assertIsNone(queue.dequeue())  # Vérifier que dequeue retourne None
        self.assertEqual(queue.length, 0)

    def test_empty_queue(self):
        queue = MyQueue(1)
        queue.dequeue()
        self.assertIsNone(queue.first)
        self.assertIsNone(queue.last)
        self.assertEqual(queue.length, 0)

    def test_enqueue_after_dequeue(self):
        queue = MyQueue(1)
        queue.dequeue()
        queue.enqueue(10)
        self.assertEqual(str(queue), "10")
        self.assertEqual(queue.length, 1)
        self.assertEqual(queue.first.data, 10)
        self.assertEqual(queue.last.data, 10)


if __name__ == "__main__":
    unittest.main()
