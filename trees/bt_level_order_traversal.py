from __future__ import annotations
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Pretty print the tree with connections
        def display(node, prefix="", is_left=True):
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

    def from_list(values: list[int | None]) -> TreeNode:
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

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        queue: deque[tuple[int, TreeNode]] = deque()
        queue.append((1, root))

        levels = []
        current_level = []

        while queue:
            level, node = queue.popleft()
            if len(current_level) > 0 and current_level[-1][0] != level:
                assert current_level[-1][0] == level - 1
                levels.append(list(map(lambda x: x[1], current_level)))
                current_level.clear()

            current_level.append((level, node.val))

            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))

        levels.append(list(map(lambda x: x[1], current_level)))
        return levels
