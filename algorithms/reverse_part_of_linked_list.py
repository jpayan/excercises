# Reverse a linked list from position m to n. Do it in one-pass.

from data_structures.linked_list import LinkedList


def reverse_part_of_linked_list(head: LinkedList, start: int, end: int) -> LinkedList:
    if not head or start == end:
        return head

    outside_pointer = LinkedList(None)
    outside_pointer.next = head

    current_node = head
    previous_node = outside_pointer

    while start > 1:
        previous_node = current_node
        current_node = current_node.next
        start -= 1
        end -= 1

    while end > 1:
        next_node = current_node.next
        current_node.next = next_node.next
        next_node.next = previous_node.next
        previous_node.next = next_node
        end -= 1
    
    return outside_pointer.next


if __name__ == '__main__':
    head = LinkedList("1")
    head.next = LinkedList("2")
    head.next.next = LinkedList("3")
    head.next.next.next = LinkedList("4")
    head.next.next.next.next = LinkedList("5")

    print(head)
    print(reverse_part_of_linked_list(head, 2, 4))
