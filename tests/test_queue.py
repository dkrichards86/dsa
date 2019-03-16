import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def tearDown(self):
        self.queue = None

    def test_enqueue(self):
        self.queue.enqueue("foo")
        self.assertTrue(self.queue.queue.head.data == "foo")
        self.assertTrue(self.queue.queue.head.next is None)

        self.queue.enqueue("bar")
        self.assertTrue(self.queue.queue.head.data == "foo")
        self.assertTrue(self.queue.queue.head.next.data == "bar")

    def test_deque(self):
        self.queue.enqueue("foo")
        self.queue.enqueue("bar")

        self.assertTrue(self.queue.queue.head.data == "foo")
        self.assertTrue(self.queue.queue.head.next.data == "bar")
        
        self.queue.dequeue()
        self.assertTrue(self.queue.queue.head.data == "bar")
        self.assertTrue(self.queue.queue.head.next is None)


if __name__ == '__main__':
    unittest.main()
