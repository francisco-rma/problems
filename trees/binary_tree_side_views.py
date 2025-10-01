from __future__ import annotations
from collections import deque
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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
    def lst_from_list(values: list[int | None]) -> TreeNode | None:
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

    @staticmethod
    def rst_from_list(values: list[int | None]) -> TreeNode | None:
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

            right_val = queue.popleft()
            if right_val:
                cur_node.right = TreeNode(right_val)
                nodes.append(cur_node.right)

            if queue:
                left_val = queue.popleft()
                if left_val:
                    cur_node.left = TreeNode(left_val)
                    nodes.append(cur_node.left)

        return root

    @staticmethod
    def right_side_view(root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        queue = deque([(root.right, 2), (root.left, 2)])
        result = [root.val]

        traversed_levels = set([1])

        i = 0
        while queue:
            i += 1
            node, level = queue.popleft()
            if not node:
                continue

            assert type(node) == TreeNode
            assert type(level) == int

            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

            if level not in traversed_levels:
                result.append(node.val)
                traversed_levels.add(level)

        return result

    @staticmethod
    def left_side_view(root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        queue = deque([(root.left, 2), (root.right, 2)])
        result = [root.val]

        traversed_levels = set([1])

        i = 0
        while queue:
            i += 1
            node, level = queue.popleft()
            if not node:
                continue

            assert type(node) == TreeNode
            assert type(level) == int

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

            if level not in traversed_levels:
                result.append(node.val)
                traversed_levels.add(level)

        return result

    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        result = root.right_side_view()
        return result


if __name__ == "__main__":
    samples = [
        [1, 2, 3, None, 5, None, 4],
        [1, 2, 3, 4, None, None, None, 5],
        [1, None, 3],
        [],
        [None],
        [1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7],
    ]

    for sample in samples:
        root: TreeNode = TreeNode.lst_from_list(values=sample)
        print(f"\nRoot:\n{root}")

        result_right = TreeNode.right_side_view(root)
        print("result_right: ", result_right)
        result_left = TreeNode.left_side_view(root)
        print("result_left: ", result_left)
