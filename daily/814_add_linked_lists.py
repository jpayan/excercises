"""
[EASY]
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node
represent a digit in the number. The nodes make up the number in reversed
order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list
format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""
from data_structures.linked_list import LinkedList


def add_linked_lists(n1: LinkedList, n2: LinkedList) -> LinkedList:
    result = LinkedList(None)
    temp = result
    carry_over = 0
    while n1 is not None or n1 is not None or carry_over > 0:
        if n1 is not None:
            carry_over += n1.value
            n1 = n1.next
        if n2 is not None:
            carry_over += n2.value
            n2 = n2.next
        carry_over, next_value = divmod(carry_over, 10)
        temp.next = temp = LinkedList(next_value)
    return result.next


if __name__ == '__main__':
    ninety_nine = LinkedList(9)
    ninety_nine.next = LinkedList(9)

    twenty_five = LinkedList(5)
    twenty_five.next = LinkedList(2)

    hundred_twenty_four = LinkedList(4)
    hundred_twenty_four.next = LinkedList(2)
    hundred_twenty_four.next.next = LinkedList(1)

    assert add_linked_lists(ninety_nine, twenty_five) == hundred_twenty_four
