from data_structures.linked_list import LinkedList


def reverse_linked_list(head: LinkedList) -> LinkedList:
    current_node = head
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


if __name__ == '__main__':
    a = LinkedList('a')
    b = LinkedList('b')
    c = LinkedList('c')
    d = LinkedList('d')
    e = LinkedList('e')

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print(a)
    print(reverse_linked_list(a))
