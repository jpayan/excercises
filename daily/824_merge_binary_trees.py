"""
[EASY]
This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should
hold a value equal to the sum of the values of the corresponding nodes of the
input trees.

If only one input tree has a node in a given position, the corresponding node
in the new tree should match that input node.
"""
from data_structures.binary_tree import BinaryTree


def merge_binary_trees(b1: BinaryTree, b2: BinaryTree) -> BinaryTree:
    if b1 and b2:
        root = BinaryTree(b1.value + b2.value)
        root.left = merge_binary_trees(b1.left, b2.left)
        root.right = merge_binary_trees(b1.right, b2.right)
        return root
    else:
        return b1 or b2


if __name__ == '__main__':
    tree1 = BinaryTree(3)
    tree1.left = BinaryTree(2)
    tree1.right = BinaryTree(1)
    tree1.display()

    tree2 = BinaryTree(5)
    tree2.left = BinaryTree(3)
    tree2.right = BinaryTree(2)
    tree2.right.right = BinaryTree(1)
    tree2.display()

    merged_tree = merge_binary_trees(tree1, tree2)
    merged_tree.display()
