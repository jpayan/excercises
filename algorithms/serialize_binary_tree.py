# Serialize a binary tree
from typing import List, Any

from data_structures.binary_tree import BinaryTree


def serialize_binary_tree(root: BinaryTree, serialized_tree: List[Any]=[]) -> List[Any]:
    if root:
        serialized_tree.append(root.value)
        serialize_binary_tree(root.left, serialized_tree)
        serialize_binary_tree(root.right, serialized_tree)
    else:
        serialized_tree.append(None)
    return serialized_tree


def deserialize_binary_tree(serialized_tree: List[Any]) -> BinaryTree:
    current_value = serialized_tree.pop(0)
    if current_value:
        root = BinaryTree(current_value)
        root.left = deserialize_binary_tree(serialized_tree)
        root.right = deserialize_binary_tree(serialized_tree)
        return root


if __name__ == '__main__':
    root = BinaryTree(6)
    root.left = BinaryTree(4)
    root.left.left = BinaryTree(2)
    root.left.left.left = BinaryTree(1)
    root.left.left.right = BinaryTree(3)
    root.left.right = BinaryTree(5)
    root.right = BinaryTree(9)
    root.right.left = BinaryTree(7)
    root.right.left.right = BinaryTree(8)
    root.right.right = BinaryTree(10)

    root.display()
    serialized_binary_tree = serialize_binary_tree(root)
    print(serialized_binary_tree)

    root = deserialize_binary_tree(serialized_binary_tree)
    root.display()
