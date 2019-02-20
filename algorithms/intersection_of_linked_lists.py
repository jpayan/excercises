# Write a program to find the node at which the intersection of two singly linked lists begins.

def get_intersection_node(headA, headB):
    pointer_1 = headA
    pointer_2 = headB
    
    while pointer_1 is not pointer_2:
        pointer_1 = headB if pointer_1 is None else pointer_1.next 
        pointer_2 = headA if pointer_2 is None else pointer_2.next
    
    return pointer_1

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return "{} -> {}".format(self.value, self.next)


intersection = Node(3, Node(4, Node(5)))
headA = Node(3, Node(7, intersection))
headB = Node(5, intersection)

print(get_intersection_node(headA, headB))