# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
# The program should run in O(1) space complexity and O(nodes) time complexity.
from data_structures.linked_list import LinkedList


def order_linked_list_by_odd_even(head_odd: LinkedList) -> None:
    if not head_odd or not head_odd.next:
        return

    head_even = head_odd.next
    current_even = head_even
    current_odd = head_odd

    while current_even and current_even.next:
        current_odd.next = current_even.next
        current_odd = current_odd.next
        current_even.next = current_odd.next
        current_even = current_even.next

    current_odd.next = head_even


if __name__ == '__main__':

    linked_list = LinkedList(1)
    current_node = linked_list
    for i in range(10):
        current_node.next = LinkedList(i + 2)
        current_node = current_node.next

    print(linked_list)
    order_linked_list_by_odd_even(linked_list)
    print(linked_list)
