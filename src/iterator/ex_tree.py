"""
Iterator Design Pattern Example: Tree Traversal 
"""

from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable

class TreeNode:
    """Represents a node in a binary tree."""

    def __init__(self, value: int) -> None:
        """
        Initializes a TreeNode with a value.
        """
        self.value = value
        self.left = None
        self.right = None

class TreeIterator(Iterator, ABC):
    """Abstract base class for tree iterators."""

    def __init__(self, root: TreeNode) -> None:
        """
        Initializes the iterator with the root of the tree.
        """
        self.stack = []
        self._initialize_stack(root)

    @abstractmethod
    def _initialize_stack(self, node: TreeNode) -> None:
        """
        Initializes the stack for traversal.

        Args:
            node (TreeNode): The current node.
        """
        pass

    @abstractmethod
    def __next__(self) -> int:
        """Returns the next value in the traversal."""
        pass

class InOrderIterator(TreeIterator):
    """Iterator for in-order traversal of a binary tree."""

    def _initialize_stack(self, node: TreeNode) -> None:
        """Initializes the stack for in-order traversal."""
        self._push_left(node)

    def _push_left(self, node: TreeNode) -> None:
        """Pushes all left children of a node onto the stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def __next__(self) -> int:
        """Returns the next value in the in-order traversal."""
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        self._push_left(node.right)
        return node.value

class InvertingIterator(TreeIterator):
    """Iterator for reverse in-order traversal of a binary tree."""

    def _initialize_stack(self, node: TreeNode) -> None:
        """Initializes the stack for reverse in-order traversal."""
        self._push_right(node)

    def _push_right(self, node: TreeNode) -> None:
        """Pushes all right children of a node onto the stack."""
        while node:
            self.stack.append(node)
            node = node.right

    def __next__(self) -> int:
        """Returns the next value in the reverse in-order traversal."""
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        self._push_right(node.left)
        return node.value

class BFSIterator(TreeIterator):
    """Iterator for breadth-first traversal of a binary tree."""

    def _initialize_stack(self, node: TreeNode) -> None:
        """Initializes the queue for breadth-first traversal."""
        if node:
            self.stack.append(node)

    def __iter__(self) -> Iterator[int]:
        """Returns the iterator itself."""
        return self

    def __next__(self) -> int:
        """Returns the next value in the breadth-first traversal."""
        if not self.stack:
            raise StopIteration
        current_node = self.stack.pop(0)
        if current_node.left:
            self.stack.append(current_node.left)
        if current_node.right:
            self.stack.append(current_node.right)
        return current_node.value

class TreeIterable(Iterable):
    """Iterable collection of tree nodes."""

    def __init__(self, root: TreeNode) -> None:
        """Initializes the iterable with the root of the tree."""
        self.root = root

    def __iter__(self) -> Iterator[int]:
        """Returns an iterator for in-order traversal."""
        return InOrderIterator(self.root)

    def inverting_iterator(self) -> Iterator[int]:
        """Returns an iterator for reverse in-order traversal."""
        return InvertingIterator(self.root)

    def bfs_iterator(self) -> Iterator[int]:
        """Returns an iterator for breadth-first traversal."""
        return BFSIterator(self.root)

def print_tree(root: TreeNode) -> None:
    """Prints the tree in a level-order format."""
    if not root:
        return

    levels = {}
    queue = [(root, 0)]

    while queue:
        node, level = queue.pop(0)
        if level not in levels:
            levels[level] = []
        levels[level].append(node.value if node else None)

        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

    max_level = max(levels.keys())
    max_width = 2 ** max_level

    for level in range(max_level + 1):
        level_nodes = levels[level]
        gap = ' ' * (max_width // (2 ** level))
        line = gap.join(str(node) if node is not None else ' ' for node in level_nodes)
        print(gap + line + gap)


if __name__ == "__main__":
    # Usage
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print_tree(root)

    tree_iterable = TreeIterable(root)

    print("InOrder Traversal:")
    for value in tree_iterable:
        print(value)

    print("\nInverting Traversal (Reverse InOrder):")
    for value in tree_iterable.inverting_iterator():
        print(value)

    print("\nBFS Traversal:")
    for value in tree_iterable.bfs_iterator():
        print(value)
