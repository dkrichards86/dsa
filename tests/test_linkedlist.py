import unittest
from src.linkedlist import SinglyLinkedList, DoublyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkedList()

    def tearDown(self):
        self.list = None

    def test_prepend(self):
        self.list.prepend("foo")
        self.assertTrue(self.list.head.data == "foo")
        self.assertTrue(self.list.head.next is None)

        self.list.prepend("bar")
        self.assertTrue(self.list.head.data == "bar")
        self.assertTrue(self.list.head.next.data == "foo")

    def test_append(self):
        self.list.append("foo")

        self.assertTrue(self.list.head.data == "foo")
        self.assertTrue(self.list.head.next is None)
        
        self.list.append("bar")
        self.assertTrue(self.list.head.data == "foo")
        self.assertTrue(self.list.head.next.data == "bar")

    def test_insert_at(self):
        self.list.append("foo")
        self.list.append("bar")

        self.assertTrue(self.list.head.data == "foo")
        self.assertTrue(self.list.head.next.data == "bar")

        self.list.insert_at("baz", 1)
        self.assertTrue(self.list.head.next.data == "baz")
        
        with self.assertRaises(IndexError):
            self.list.insert_at("qux", 8)

    def test_next(self):
        self.list.append("foo")
        self.list.append("bar")
        self.list.append("baz")

        self.assertTrue(self.list.head.data == "foo")

        head_next = self.list.head.next
        self.assertTrue(head_next.data == "bar")

        last = head_next.next
        self.assertTrue(last.data == "baz")

    def test_find(self):
        self.list.prepend("foo")
        self.list.prepend("bar")

        found = self.list.find("foo")
        self.assertTrue(found.data == "foo")

        found = self.list.find("bar")
        self.assertTrue(found.data == "bar")

        with self.assertRaises(ValueError):
            self.list.find("baz")

    def test_find_at(self):
        self.list.append("foo")
        self.list.append("bar")

        found = self.list.find_at(0)
        self.assertTrue(found.data == "foo")

        found = self.list.find_at(1)
        self.assertTrue(found.data == "bar")

        with self.assertRaises(IndexError):
            self.list.find_at(8)

    def test_delete(self):
        self.list.prepend("foo")
        self.list.prepend("bar")
        self.list.prepend("baz")

        self.assertTrue(self.list.head.data == "baz")

        # Delete the list head
        self.list.delete("baz")
        self.assertTrue(self.list.head.data == "bar")

        # Delete the list tail
        self.list.delete("foo")
        self.assertTrue(self.list.head.next is None)

    def test_delete_at(self):
        self.list.append("foo")
        self.list.append("bar")
        self.list.append("baz")
        self.list.append("qux")

        self.assertTrue(self.list.head.data == "foo")

        self.list.delete_at(0)
        self.assertTrue(self.list.head.data == "bar")

        self.list.delete_at(1)
        self.assertTrue(self.list.head.next.data == "qux")

    def test_delete_value_not_in_list(self):
        self.list.prepend("foo")
        self.list.prepend("bar")

        with self.assertRaises(ValueError):
            self.list.delete("baz")

    def test_delete_empty_list(self):
        with self.assertRaises(ValueError):
            self.list.delete("foo")

    def test_delete_next_reassignment(self):
        self.list.prepend("foo")
        self.list.prepend("bar")
        self.list.prepend("baz")
        self.list.prepend("foobar")

        self.list.delete("baz")
        self.list.delete("bar")

        self.assertTrue(self.list.head.next.data == "foo")

    def test_size(self):
        self.list.prepend("foo")
        self.list.prepend("bar")
        self.list.prepend("baz")
        self.assertEqual(self.list.size, 3)
        
        self.list.delete("baz")
        self.assertEqual(self.list.size, 2)


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def tearDown(self):
        self.list = None

    def test_prepend(self):
        self.list.prepend("foo")
        self.assertTrue(self.list.head.data == "foo")
        self.assertTrue(self.list.head.next is None)
        self.assertTrue(self.list.head.prev is None)

        self.list.prepend("bar")
        self.assertTrue(self.list.head.data == "bar")
        self.assertTrue(self.list.head.next.data == "foo")
        self.assertTrue(self.list.head.next.prev.data == "bar")

        self.list.prepend("baz")
        self.assertTrue(self.list.head.data == "baz")
        self.assertTrue(self.list.head.next.data == "bar")
        self.assertTrue(self.list.head.next.prev.data == "baz")

    def test_append(self):
        self.list.append("foo")

        self.assertTrue(self.list.head.data == "foo")
        self.assertTrue(self.list.head.next is None)
        self.assertTrue(self.list.head.prev is None)

        self.list.append("bar")
        self.assertTrue(self.list.head.data == "foo")
        self.assertTrue(self.list.head.next.data == "bar")
        self.assertTrue(self.list.head.next.prev.data == "foo")

    def test_insert_at(self):
        self.list.append("foo")
        self.list.append("bar")

        self.assertTrue(self.list.head.data == "foo")
        self.assertTrue(self.list.head.next.data == "bar")
        self.assertTrue(self.list.head.prev is None)

        self.list.insert_at("baz", 1)
        self.assertTrue(self.list.head.next.data == "baz")
        self.assertTrue(self.list.head.next.prev.data == "foo")

    def test_next(self):
        self.list.append("foo")
        self.list.append("bar")
        self.list.append("baz")

        self.assertTrue(self.list.head.data == "foo")

        head_next = self.list.head.next
        self.assertTrue(head_next.data == "bar")

        last = head_next.next
        self.assertTrue(last.data == "baz")

    def test_prev(self):
        self.list.append("foo")
        self.list.append("bar")

        self.assertTrue(self.list.head.data == "foo")

        head_prev = self.list.head.prev
        self.assertTrue(head_prev is None)

        next_prev = self.list.head.next.prev
        self.assertTrue(next_prev.data == "foo")

    def test_find(self):
        self.list.prepend("foo")
        self.list.prepend("bar")

        found = self.list.find("foo")
        self.assertTrue(found.data == "foo")

        found = self.list.find("bar")
        self.assertTrue(found.data == "bar")

        with self.assertRaises(ValueError):
            self.list.find("baz")

    def test_find_at(self):
        self.list.append("foo")
        self.list.append("bar")

        found = self.list.find_at(0)
        self.assertTrue(found.data == "foo")

        found = self.list.find_at(1)
        self.assertTrue(found.data == "bar")

        with self.assertRaises(IndexError):
            self.list.find_at(8)

    def test_delete(self):
        self.list.append("foo")
        self.list.append("bar")
        self.list.append("baz")

        self.assertTrue(self.list.head.data == "foo")

        # Delete the list head
        self.list.delete("foo")
        self.assertTrue(self.list.head.data == "bar")

        # Delete the list tail
        self.list.delete("baz")
        self.assertTrue(self.list.head.next is None)

        self.list.append("qux")
        self.list.append("quuz")

        head_next = self.list.head.next
        self.assertTrue(head_next.data == "qux")
        self.assertTrue(head_next.next.data == "quuz")
        self.assertTrue(head_next.prev.data == "bar")

    def test_delete_at(self):
        self.list.append("foo")
        self.list.append("bar")
        self.list.append("baz")
        self.list.append("qux")

        self.assertTrue(self.list.head.data == "foo")

        self.list.delete_at(0)
        self.assertTrue(self.list.head.data == "bar")

        self.list.delete_at(1)
        self.assertTrue(self.list.head.next.data == "qux")
        self.assertTrue(self.list.head.next.prev.data == "bar")

    def test_delete_value_not_in_list(self):
        self.list.prepend("foo")
        self.list.prepend("bar")

        with self.assertRaises(ValueError):
            self.list.delete("baz")

    def test_delete_next_reassignment(self):
        self.list.prepend("foo")
        self.list.prepend("bar")
        self.list.prepend("baz")
        self.list.prepend("qux")

        self.list.delete("baz")
        self.list.delete("bar")

        self.assertTrue(self.list.head.data == "qux")
        self.assertTrue(self.list.head.next.data == "foo")

    def test_delete_prev_reassignment(self):
        self.list.append("foo")
        self.list.append("bar")
        self.list.append("baz")
        self.list.append("qux")
        self.list.append("quuz")

        self.list.delete("baz")
        self.list.delete("bar")

        head_next = self.list.head.next
        self.assertTrue(head_next.data == "qux")
        self.assertTrue(head_next.prev.data == "foo")

    def test_size(self):
        self.list.prepend("foo")
        self.list.prepend("bar")
        self.list.prepend("baz")
        self.assertEqual(self.list.size, 3)
        
        self.list.delete("baz")
        self.assertEqual(self.list.size, 2)


if __name__ == '__main__':
    unittest.main()
