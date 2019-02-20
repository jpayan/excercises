# Merge a linked list into another linked list at alternate positions

def merge_linked_lists(linked_list_1, linked_list_2):
    if linked_list_1:
        linked_list_3 = linked_list_1
        linked_list_3.next = merge_linked_lists(linked_list_2, linked_list_1.next)
        return linked_list_3
    if not linked_list_1 and linked_list_2:
        return linked_list_2

class Node():
    def __init__(self, value, next_value = None):
        self.value = value
        self.next = next_value
    
    def __repr__(self):
        return "{} -> {}".format(self.value, self.next)

# linked_list_1 = Node("0", Node("2", Node("4", Node("6", Node("8")))))
linked_list_1 = Node("0", Node("2", Node("4", Node("6", Node("8", Node("11", Node("13")))))))
# linked_list_2 = Node("1", Node("3", Node("5", Node("7", Node("9", Node("10", Node("12")))))))
linked_list_2 = Node("1", Node("3", Node("5", Node("7", Node("9")))))

print(linked_list_1)
print(linked_list_2)

merge_linked_lists(linked_list_1, linked_list_2)

print(linked_list_1)
