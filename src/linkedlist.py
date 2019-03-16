class SinglyLinkedListNode():
    def __init__(self):
        self.data = None
        self.next = None


class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, value):
        """
        Add an element at the head of the list. Point the new element's 'next'
        at the previous head, shifting all remaining elements to the right.

        :param value: data to add
        """
        new_node = SinglyLinkedListNode()
        new_node.data = value
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, value):
        """
        Add an element at the tail of the list. Update the previous final
        element's 'next' to point to the new element.

        :param value: data to add
        """
        new_node = SinglyLinkedListNode()
        new_node.data = value
        curr_node = self.head
        prev_node = None

        while curr_node is not None:
            prev_node = curr_node
            curr_node = curr_node.next

        if prev_node:
            prev_node.next = new_node
        else:
            self.head = new_node

        self.size += 1

    def insert(self, value):
        """
        Insert an element in the list.

        This method exists for convenient naming.

        :param value: data to add
        """
        self.prepend(value)

    def insert_at(self, value, position):
        """
        Insert an element at a specified position.

        This method exists for convenient naming.

        :param value: data to add
        :param position: index to insert at
        """

        if position >= self.size:
            raise IndexError

        new_node = SinglyLinkedListNode()
        new_node.data = value
        curr_node = self.head
        prev_node = None
        curr_index = 0
        while curr_index < position:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1

        if prev_node:
            prev_node.next = new_node
        else:
            curr_node.next = curr_node
            curr_node = new_node

        self.size += 1

    def find(self, value):
        """
        Find an element in the list

        :param value: data to find
        """
        curr_node = self.head

        while curr_node is not None:
            if curr_node.data == value:
                return curr_node
            curr_node = curr_node.next

        if curr_node is None:
            raise ValueError('{} not found'.format(value))

    def find_at(self, position):
        """
        Get the element at a given position

        :param position: index to retrieve
        """
        if position >= self.size:
            raise IndexError

        curr_node = self.head
        curr_index = 0
        while curr_index < position:
            curr_node = curr_node.next
            curr_index += 1

        return curr_node

    def delete(self, value):
        """
        Remove an element in the list.

        :param value: data to remove
        """
        curr_node = self.head
        prev_node = None

        # walk the list
        while curr_node is not None:
            # if we find a match, short circuit the loop.
            if curr_node.data == value:
                break
            # if we don't match, update the previous elements "pointer"
            # to the target's "next"
            else:
                prev_node = curr_node
                curr_node = curr_node.next

        # raise if we haven't found anything
        if curr_node is None:
            raise ValueError('{} not found'.format(value))

        if prev_node is not None:
            prev_node.next = curr_node.next
        else:
            self.head = curr_node.next

        self.size -= 1

    def delete_at(self, position):
        """
        Remove the element at a given index.

        :param position: index to remove
        """
        if position >= self.size:
            raise IndexError

        curr_node = self.head
        prev_node = None
        curr_index = 0

        # walk the list
        while curr_index < position:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1

        if prev_node is not None:
            prev_node.next = curr_node.next
        else:
            self.head = curr_node.next

        self.size -= 1


class DoublyLinkedListNode():
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, value):
        """
        Add an element at the head of the list. Point the new element's 'next'
        at the previous head, shifting all remaining elements to the right.

        :param value: data to add
        """
        new_node = DoublyLinkedListNode()
        new_node.data = value

        # If we have a DLL B <-> C and prepend A, we should get A <-> B <-> C
        curr_head = self.head

        new_node.next = curr_head
        new_node.prev = None

        if curr_head is not None:
            curr_head.prev = new_node

        self.head = new_node
        self.size += 1

    def append(self, value):
        """
        Add an element at the tail of the list. Update the previous final
        element's 'next' to point to the new element.

        :param value: data to add
        """
        new_node = DoublyLinkedListNode()
        new_node.data = value
        curr_node = self.head
        prev_node = None

        while curr_node is not None:
            prev_node = curr_node
            curr_node = curr_node.next

        if prev_node:
            prev_node.next = new_node
            new_node.prev = prev_node
        else:
            self.head = new_node

        self.size += 1

    def insert(self, value):
        """
        Insert an element in the list.

        This method exists for convenient naming.

        :param value: data to add
        """
        self.prepend(value)

    def insert_at(self, value, position):
        """
        Insert an element at a specified position.

        This method exists for convenient naming.

        :param value: data to add
        :param position: index to insert at
        """
        if position >= self.size:
            raise IndexError

        new_node = DoublyLinkedListNode()
        new_node.data = value
        curr_node = self.head
        prev_node = None
        curr_index = 0
        while curr_index < position:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1

        if prev_node:
            prev_node.next = new_node
            new_node.prev = prev_node
        else:
            curr_node.next = curr_node
            curr_node = new_node

        self.size += 1

    def find(self, value):
        """
        Find an element in the list

        :param value: data to find
        """
        curr_node = self.head

        while curr_node is not None:
            if curr_node.data == value:
                return curr_node
            curr_node = curr_node.next

        if curr_node is None:
            raise ValueError('{} not found'.format(value))

    def find_at(self, position):
        """
        Get the element at a given position

        :param position: index to retrieve
        """
        if position >= self.size:
            raise IndexError

        curr_node = self.head
        curr_index = 0
        while curr_index < position:
            curr_node = curr_node.next
            curr_index += 1

        return curr_node

    def delete(self, value):
        """
        Remove an element in the list.

        :param value: data to remove
        """
        curr_node = self.head
        prev_node = None

        # walk the list
        while curr_node is not None:
            # if we find a match, short circuit the loop.
            if curr_node.data == value:
                break
            # if we don't match, update the previous elements "pointer"
            # to the target's "next"
            else:
                prev_node = curr_node
                curr_node = curr_node.next

        # raise if we haven't found anything
        if curr_node is None:
            raise ValueError('{} not found'.format(value))

        if prev_node is None:
            self.head = curr_node.next
        elif prev_node is not None and curr_node.next is not None:
            prev_node.next = curr_node.next
            curr_node.next.prev = prev_node
        else:
            prev_node.next = curr_node.next

        self.size -= 1

    def delete_at(self, position):
        """
        Remove the element at a given index.

        :param position: index to remove
        """
        if position >= self.size:
            raise IndexError

        curr_node = self.head
        prev_node = None
        curr_index = 0

        # walk the list
        while curr_index < position:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1

        if prev_node is None:
            self.head = curr_node.next
        elif prev_node is not None and curr_node.next is not None:
            prev_node.next = curr_node.next
            curr_node.next.prev = prev_node
        else:
            prev_node.next = curr_node.next

        self.size -= 1
