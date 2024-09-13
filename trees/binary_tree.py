from __future__ import annotations
from typing import Sequence


class Node(object):
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = None
        self.left: Node = None
        self.right: Node = None
        if value is not None:
            self.value = value
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        pass

    def __eq__(self, comparison: Node) -> bool:
        if self.value != comparison.value:
            return False
        left_validation = self.left.__eq__(comparison.left)
        right_validation = self.right.__eq__(comparison.right)

        return left_validation and right_validation

    def __invert__(self: Node, node: Node) -> Node:
        if node is None:
            return node
        self.__invert__(node.left)
        self.__invert__(node.right)

        node.left, node.right = node.right, node.left

        return node

    # def __invert_bfs__(self: Node) -> Node:
    #     if self.left is None and self.right is None:
    #         return
    #     self.left, self.right = self.right, self.left
    #     self.left.__invert_bfs__()
    #     self.right.__invert_bfs__()

    #     return


def populate_binary_tree(values: Sequence[int], inverted=False) -> Node:
    n = len(values)

    if n == 0:
        return None

    def inner(index: int = 0):
        if index >= n or values[index] is None:
            return None

        node = Node(values[index])
        left_idx = 2 * index + 1
        right_idx = 2 * index + 2

        node.left = inner(left_idx if not inverted else right_idx)
        node.right = inner(right_idx if not inverted else left_idx)

        return node

    return inner()


def populate_binary_search_tree(values: Sequence[int], inverted=False) -> Node:
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
    if tree is None:
        return root
    root.append(tree.value)

    def inner(node: Node):
        if node is None:
            return
        has_left_node = node.left is not None
        has_right_node = node.right is not None

        left_val = node.left.value if has_left_node else None
        right_val = node.right.value if has_right_node else None

        if has_left_node and has_right_node:
            root.append(left_val if not inverted else right_val)
            root.append(right_val if not inverted else left_val)
            inner(node.left) if not inverted else inner(node.right)
            inner(node.right) if not inverted else inner(node.left)

        elif has_left_node:
            if inverted:
                root.append(right_val)
            root.append(left_val)

        elif has_right_node:
            if not inverted:
                root.append(left_val)
            root.append(right_val)

    inner(tree)

    return root
