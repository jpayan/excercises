from data_structures.linked_list import LinkedList


class Queue:
    def __init__(self):
        self._head = LinkedList(None)
        self._tail = LinkedList(None)
        self._head.next = self._tail
        self._tail.previous = self._head
        self._size = 0

    def enqueue(self, value):
        new_item = LinkedList(value)
        new_item.previous = self._head
        new_item.next = self._head.next
        self._head.next.previous = new_item
        self._head.next = new_item
        self._size += 1

    def dequeue(self):
        item = self._tail.previous
        item.previous.next = item.next
        item.next.previous = item.previous
        self._size -= 1
        return item.value

    def peek(self):
        return self._tail.previous.value

    def is_empty(self):
        return self._size == 0
