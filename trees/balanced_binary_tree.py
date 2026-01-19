from __future__ import annotations
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(
        self,
        value: int,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = value
        self.left = left
        self.right = right

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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def recursive_height(node: TreeNode, level: int = 0) -> int:
            if not node:
                return level

            left_height: int = recursive_height(node=node.left, level=level + 1)
            right_height: int = recursive_height(node=node.right, level=level + 1)

            if abs(left_height - right_height) > 1:
                self.balanced = False

            return max(left_height, right_height)

        recursive_height(node=root)

        return self.balanced


root = [1, 2, 3, None, None, 4]

tree: TreeNode = TreeNode.from_list(root)

result = tree.isBalanced(tree)

print(result)
