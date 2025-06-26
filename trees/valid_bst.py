from __future__ import annotations
from collections import deque
from typing import Optional
from trees.avl_tree import AVLNode


class TreeNode:
    def __init__(self, val: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Pretty print the tree with connections
        def display(node, prefix="", is_left=True) -> str:
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

    @staticmethod
    def from_list(values: list[int | None]) -> TreeNode | None:
        if not values:
            return None
        queue = deque(values)
        value = queue.popleft()

        while queue and value is None:
            value = queue.popleft()

        if value is None:
            return None
        root: TreeNode = TreeNode(value)
        nodes: deque[TreeNode] = deque()

        nodes.append(root)

        while queue:
            cur_node = nodes.popleft()

            left_val = queue.popleft()
            if left_val:
                cur_node.left = TreeNode(left_val)
                nodes.append(cur_node.left)

            if queue:
                right_val = queue.popleft()
                if right_val:
                    cur_node.right = TreeNode(right_val)
                    nodes.append(cur_node.right)

        return root


def validation_walk(node: TreeNode | AVLNode, min: float, max: float) -> bool:
    if not node:
        return True

    if node.val <= min or node.val >= max:
        return False

    left_valid = validation_walk(node=node.left, max=node.val, min=min) if node.left else True
    right_valid = validation_walk(node=node.right, max=max, min=node.val) if node.right else True

    return left_valid and right_valid


def isValidBST(root: Optional[TreeNode | AVLNode]) -> bool:
    if not root or not root.val:
        return True
    return validation_walk(root, float("-inf"), float("inf"))
