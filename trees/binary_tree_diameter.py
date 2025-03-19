from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, value: int, left: TreeNode = None, right: TreeNode = None):
        if not value:
            raise ValueError(f"Value cannot be {value}")
        self.value = value
        self.right = right
        self.left = left

    def from_list(values: list[int | None]) -> TreeNode:
        from collections import deque

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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs_height(origin: TreeNode) -> int:
            if not origin:
                return 0

            left_height = dfs_height(origin=origin.left)
            right_height = dfs_height(origin=origin.right)

            self.res = max(self.res, left_height + right_height)

            return max(left_height, right_height) + 1

        dfs_height(root)

        return self.res


root: TreeNode = TreeNode.from_list([1, None, 2, 3, 4, 5])
root: TreeNode = TreeNode.from_list([1, 2, 3])

result = TreeNode.diameterOfBinaryTree(root, root)

print(result)
