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

    def maxDepth(self, root: Optional[TreeNode], method: str = "dfsr") -> int:
        if not root:
            return 0

        match method:
            case "dfsr":

                def dfsr(node: Optional[TreeNode]):
                    if not node:
                        return 0
                    return 1 + max(dfsr(node=node.left), dfsr(node=node.right))

                return dfsr(root)

            case "dfsi":

                def dfsi(node: Optional[TreeNode]):
                    if not node:
                        return 0

                    from collections import deque

                    max_depth = 1
                    cur_depth = 1
                    visited: set[TreeNode] = set([node])
                    stack: deque[tuple[TreeNode, int]] = deque()
                    stack.append((node, cur_depth))

                    while stack:
                        if node and node not in visited:
                            cur_depth += 1
                            visited.add(node)

                        is_leaf = not (node.left or node.right)

                        if is_leaf:
                            max_depth = max(max_depth, cur_depth)
                            node, cur_depth = stack.pop()
                            continue

                        if node.right and node.right not in visited:
                            stack.append((node, cur_depth))
                            node = node.right
                            continue

                        if node.left and node.left not in visited:
                            stack.append((node, cur_depth))
                            node = node.left
                            continue

                        node, cur_depth = stack.pop()

                    return max_depth

                return dfsi(root)

            case _:
                return None

    def maxDepthBfs(self, root: Optional[TreeNode]): ...


root: TreeNode = TreeNode.from_list([1, 2, 3, 4, 5])

print(root.maxDepth(root=root, method="dfsi"))
