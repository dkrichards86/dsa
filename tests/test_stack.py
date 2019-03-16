import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack = None

    def test_push(self):
        self.stack.push("foo")
        self.assertTrue(self.stack.stack.head.data == "foo")
        self.assertTrue(self.stack.stack.head.next is None)

        self.stack.push("bar")
        self.assertTrue(self.stack.stack.head.data == "bar")
        self.assertTrue(self.stack.stack.head.next.data == "foo")

    def test_pop(self):
        self.stack.push("foo")
        self.stack.push("bar")

        self.assertTrue(self.stack.stack.head.data == "bar")
        self.assertTrue(self.stack.stack.head.next.data == "foo")
        
        self.stack.pop()
        self.assertTrue(self.stack.stack.head.data == "foo")
        self.assertTrue(self.stack.stack.head.next is None)


if __name__ == '__main__':
    unittest.main()
