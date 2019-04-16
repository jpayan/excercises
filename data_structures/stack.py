from data_structures.linked_list import LinkedList


class Stack:
    def __init__(self):
        self._head = LinkedList(None)
        self.size = 0

    def push(self, value):
        item = LinkedList(value)
        item.next = self._head.next
        self._head.next = item
        self.size += 1

    def pop(self):
        item = self._head.next
        self._head.next = item.next
        self.size -= 1
        return item.value

    def peek(self):
        return self._head.next.value

    def __str__(self):
        items = []
        current_node = self._head.next
        while current_node is not None:
            items.append(current_node.value)
            current_node = current_node.next
        return str(items)
