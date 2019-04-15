# Serialize a binary tree
import ast
from typing import List, Any

from data_structures.binary_tree import BinaryTree


def serialize_binary_tree(root: BinaryTree) -> str:
    serialized_tree = []
    _serialize_binary_tree(root, serialized_tree)
    return str(serialized_tree)


# Encapsulating the recursive method to prevent any stored result manipulation (serialized_tree)
def _serialize_binary_tree(root: BinaryTree, serialized_tree: List[Any]) -> None:
    if root:
        serialized_tree.append(root.value)
        _serialize_binary_tree(root.left, serialized_tree)
        _serialize_binary_tree(root.right, serialized_tree)
    else:
        serialized_tree.append(None)


def deserialize_binary_tree(serialized_tree: str) -> BinaryTree:
    return _deserialize_binary_tree(ast.literal_eval(serialized_tree))


def _deserialize_binary_tree(serialized_tree: List[Any]) -> BinaryTree:
    current_value = serialized_tree.pop(0)
    if current_value:
        root = BinaryTree(current_value)
        root.left = _deserialize_binary_tree(serialized_tree)
        root.right = _deserialize_binary_tree(serialized_tree)
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
