from src.linkedlist import SinglyLinkedList


class Queue():
    def __init__(self):
        self.queue = SinglyLinkedList()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        node = self.queue.find_at(0)
        self.queue.delete_at(0)
        return node

    def is_empty(self):
        return self.queue.size == 0
