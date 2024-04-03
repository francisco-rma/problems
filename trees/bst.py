from __future__ import annotations
from typing import Sequence


class Node(object):

    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = None
        self.left = None
        self.right = None
        if value is not None:
            self.value = value
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        pass

    def search(self, target: int):
        if self.value == target:
            return self
        elif self.children is None or len(self.children) <= 0:
            return None
        else:
            for child in self.children:
                test = child.search(target)
                if test is None:
                    continue
                else:
                    return test

    def __eq__(self, comparison: Node) -> bool:
        if self.value != comparison.value:
            return False
        left_validation = self.left.__eq__(comparison.left)
        right_validation = self.right.__eq__(comparison.right)

        return left_validation and right_validation

    def add_child(self, child):
        if isinstance(child, Node):
            self.children.append(child)
        else:
            self.children.append(Node(child))


def populate_bst(values: Sequence[int], inverted=False) -> Node:
    n = len(values)

    if n == 0:
        return None

    def inner(index: int = 0):
        if index >= n or values[index] is None:
            return None

        node = Node(values[index])

        max_idx = None
        min_idx = None

        if 2 * index + 1 >= n:
            min_idx = 2 * index + 1
            max_idx = 2 * index + 2

        elif values[2 * index + 1] > values[2 * index + 2]:
            min_idx = 2 * index + 2
            max_idx = 2 * index + 1

        else:
            min_idx = 2 * index + 1
            max_idx = 2 * index + 2

        if inverted:
            min_idx, max_idx = max_idx, min_idx

        node.left = inner(min_idx)
        node.right = inner(max_idx)

        return node

    return inner()


def generate_root(tree: Node, inverted=False) -> Sequence[int]:
    root = []
    root.append(tree.value)

    def inner(node: Node):
        has_left_node = node.left is not None
        has_right_node = node.right is not None

        if has_left_node:
            root.append(node.left.value)

        if has_right_node:
            root.append(node.right.value)

        if has_left_node:
            inner(node.left)

        if has_right_node:
            inner(node.right)

    inner(tree)

    return root
