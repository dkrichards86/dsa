from src.linkedlist import SinglyLinkedList


class Stack():
    def __init__(self):
        self.stack = SinglyLinkedList()

    def push(self, value):
        self.stack.prepend(value)

    def pop(self):
        node = self.stack.find_at(0)
        self.stack.delete_at(0)
        return node

    def is_empty(self):
        return self.stack.size == 0
