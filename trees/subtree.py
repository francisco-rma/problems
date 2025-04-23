from __future__ import annotations
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.left: TreeNode = None
        self.right: TreeNode = None

    def from_list(values: list[int]) -> TreeNode:
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


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def inner(node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:
        if not node:
            return not bool(subNode)
        if not subNode:
            return not bool(node)

        if node.val != subNode.val:
            return False

        result = False

        result = inner(node.left, subNode.left)

        if result:
            result = inner(node.right, subNode.right)

        return result

    def dfs(node: Optional[TreeNode], target: int) -> bool:
        if not node:
            return False

        result = False

        if node.val == target:
            result = inner(node, subRoot)

        if result or dfs(node.left, target) or dfs(node.right, target):
            return True

        return False

    return dfs(root, subRoot.val)


root = [1, 2, 3, 4, 5]
subRoot = [2, 4, 5]
root = [1, 2, 3, 4, 5, None, None, 6]
subRoot = [2, 4, 5]

tree = TreeNode.from_list(root)
subTree = TreeNode.from_list(subRoot)

result = isSubtree(tree, subTree)
print(result)
