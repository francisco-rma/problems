from __future__ import annotations
from collections import deque
from typing import Optional


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

    def from_list(values: list[int | None]) -> TreeNode | None:
        if not values:
            return None
        queue = deque(values)
        value = queue.popleft()
        root = TreeNode(value)
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


def good_node_count(node: TreeNode, min_val: float, count: int) -> int:
    if not node:
        return 0

    left_count = (
        good_node_count(node=node.left, min_val=max(min_val, node.val), count=count)
        if node.left
        else 0
    )

    right_count = (
        good_node_count(node=node.right, min_val=max(min_val, node.val), count=count)
        if node.right
        else 0
    )

    if node.val >= min_val:
        count += 1

    return count + left_count + right_count


def goodNodes(root: Optional[TreeNode]) -> int:
    return good_node_count(node=root, min_val=float("-inf"), count=0)
