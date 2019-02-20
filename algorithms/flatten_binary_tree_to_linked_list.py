# Given a binary tree, flatten it to a linked list in-place.
from data_structures.binary_tree import BinaryTree


class TreeFlattener:
    def __init__(self, tree: BinaryTree) -> None:
        self.previous = None
        self._flatten(tree)
        self.previous = None

    def _flatten(self, root: BinaryTree) -> None:
        if root:
            self._flatten(root.right)
            self._flatten(root.left)

            root.right = self.previous
            root.left = None
            self.previous = root


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.left = BinaryTree(3)
    root.left.right = BinaryTree(4)
    root.right = BinaryTree(5)
    root.right.right = BinaryTree(6)

    root.display()
    print("\n")
    TreeFlattener(root)
    root.display()
