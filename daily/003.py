"""
Asked by Google

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string back
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    serilized_tree = []
    _serialize(root, serilized_tree)
    return str(serilized_tree)


def _serialize(root, serialized_tree):
    if root:
        serialized_tree.append(root.val)
        _serialize(root.left, serialized_tree)
        _serialize(root.right, serialized_tree)
    else:
        serialized_tree.append(None)


def deserialize(serialized_tree):
    return _deserialize(eval(serialized_tree))


def _deserialize(serialized_tree):
    current_value = serialized_tree.pop(0)
    if current_value:
        root = Node(current_value)
        root.left = _deserialize(serialized_tree)
        root.right = _deserialize(serialized_tree)
        return root

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
