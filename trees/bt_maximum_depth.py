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

            case "bfsi":

                def bfsi(node: Optional[TreeNode]):
                    from collections import deque

                    queue = deque([node])
                    visited = set()
                    level = 0

                    while queue:
                        for _ in range(len(queue)):
                            node = queue.popleft()
                            if node.left:
                                queue.append(node.left)
                            if node.right:
                                queue.append(node.right)
                        level += 1

                    for node in visited:
                        print(f"visited {node.value} at {node}")
                    return level

                return bfsi(root)

            case _:
                return None

    def maxDepthBfs(self, root: Optional[TreeNode]): ...


root: TreeNode = TreeNode.from_list([1, 2, None, 3, None, 4, None, 5])

print(root.maxDepth(root=root, method="bfsi"))
