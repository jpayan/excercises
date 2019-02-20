from data_structures.linked_list import LinkedList
from data_structures.stack import Stack


def is_palindrome(head: LinkedList) -> bool:
    current_node = head
    stack = Stack()

    while current_node:
        stack.push(current_node)
        current_node = current_node.next

    while head:
        if head.value != stack.pop().value:
            return False
        head = head.next
    return True


if __name__ == '__main__':

    linked_list = LinkedList("S")
    linked_list.next = LinkedList("A")
    linked_list.next.next = LinkedList("M")
    linked_list.next.next.next = LinkedList("L")
    print(is_palindrome(linked_list))

    linked_list = LinkedList("A")
    linked_list.next = LinkedList("B")
    linked_list.next.next = LinkedList("B")
    linked_list.next.next.next = LinkedList("A")
    print(is_palindrome(linked_list))
