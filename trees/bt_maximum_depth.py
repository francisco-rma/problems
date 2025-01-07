from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(
        self, value: int = None, left: TreeNode = None, right: TreeNode = None
    ):
        self.value = value
        self.right = right
        self.left = left

    def from_list(values: list[int | None]) -> TreeNode:
        n = len(values)

        def inner(idx: int = 0):
            if idx >= n or values[idx] is None:
                return None
            node = TreeNode(value=values[idx])
            node.left = inner(2 * idx + 1)
            node.right = inner(2 * idx + 2)

            return node

        return inner()

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode], level: int = 0):
            max_depth = level + 1
            if not (node.left or node.right):
                print(f"Max depth so far is {max_depth}")
                return max_depth
            if node.left:
                max_depth = max(max_depth, dfs(node=node.left, level=level + 1))
            if node.right:
                max_depth = max(max_depth, dfs(node=node.right, level=level + 1))

            return max_depth

        return dfs(root, level=0)


root: TreeNode = TreeNode.from_list([1, 2, 3, 4, 5])

print(root.maxDepth(root=root))
