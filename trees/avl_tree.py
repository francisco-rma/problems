from __future__ import annotations
from collections import deque
from typing import Optional


class AVLNode:
    def from_list(values: list[int | None]) -> AVLNode | None:
        if not values:
            return None
        queue = deque(values)
        value = queue.popleft()
        root = AVLNode(value)
        nodes: deque[AVLNode] = deque()

        nodes.append(root)

        while queue:
            cur_node = nodes.popleft()

            left_val = queue.popleft()
            if left_val:
                cur_node.left = AVLNode(left_val)
                nodes.append(cur_node.left)

            if queue:
                right_val = queue.popleft()
                if right_val:
                    cur_node.right = AVLNode(right_val)
                    nodes.append(cur_node.right)

        return root

    def __init__(self, val: int, left: Optional[AVLNode] = None, right: Optional[AVLNode] = None):
        """Initialize an AVL tree node."""
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

    def __repr__(self):
        # Pretty print the tree with connections
        def display(node: AVLNode, prefix="", is_left=True) -> str:
            if not node:
                return ""
            result = ""
            if node.right:
                new_prefix = prefix + ("│   " if is_left else "    ")
                result += display(node.right, new_prefix, False)
            result += prefix
            if prefix:
                result += "└── " if is_left else "┌── "
            result += f"{node.val}\n"
            if node.left:
                new_prefix = prefix + ("    " if is_left else "│   ")
                result += display(node.left, new_prefix, True)
            return result

        return display(self).rstrip()

    def contains(self, target: int) -> bool:
        if not self:
            return False

        if self.val == target:
            return True

        left = self.left.contains(target=target) if self.left else False
        right = self.right.contains(target=target) if self.right else False

        return left or right

    def binary_search(self, target: int) -> tuple[AVLNode | None, AVLNode | None]:
        """Binary search to find a target value."""
        if not self:
            return False

        node = self
        parent = None
        while node:
            if node.val == target:
                return node, parent
            elif target < node.val:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        return node, parent

    def insert(self, key: int) -> tuple[AVLNode, AVLNode]:
        """Insert a new key into the AVL tree."""
        # node, parent = self.binary_search(target=key)
        # if not node:
        #     assert parent.left is None and parent.right is None, "Parent should be a leaf node"

        #     if key <= parent.val:
        #         parent.left = AVLNode(key)
        #         return parent.left, parent

        #     if key > parent.val:
        #         parent.right = AVLNode(key)
        #         return parent.right, parent

        node: AVLNode | None = self
        parent: AVLNode | None = None
        print(f"Insertion target: {key}")
        while node:
            if key == node.val:
                parent = node
                break
            elif key < node.val:
                parent = node
                node = node.left
            elif key > node.val:
                parent = node
                node = node.right

        if key == parent.val:
            return node, parent
        elif key <= parent.val:
            parent.left = AVLNode(key)
            return parent.left, parent
        elif key > parent.val:
            parent.right = AVLNode(key)
            return parent.right, parent
