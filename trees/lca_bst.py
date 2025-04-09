# lca stands for lowest common ancestor,
# bst stands for binary search tree
from __future__ import annotations

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def from_list(values: list[int]):
        n = len(values)
        if n == 0:
            return None

        def inner(idx: int) -> Optional[TreeNode]:
            if idx >= n or values[idx] is None:
                return None

            node = TreeNode(val=values[idx])
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2

            node.left = inner(left_idx)
            node.right = inner(right_idx)

            return node

        return inner(0)

    def seek(node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def inner(node: Optional[TreeNode], target: int):
            if not node:
                return None

            if node.val == target:
                return node

            left = inner(node.left, target=target)
            right = inner(node.right, target=target)

            if left is not None and right is not None:
                raise ValueError("values are not unique")
            elif left is not None:
                return left
            elif right is not None:
                return right

        return inner(node=node, target=target)

    def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def ascendancy(node: Optional[TreeNode], target: int) -> deque[TreeNode]:
            if not node:
                return None
            if node.val == target:
                return deque([node])

            result = []
            if target < node.val:
                result = ascendancy(node=node.left, target=target)
            else:
                result = ascendancy(node=node.right, target=target)

            result.appendleft(node)

            return deque(dict.fromkeys(result))

        asc_p = ascendancy(root, target=p.val)
        asc_q = ascendancy(root, target=q.val)

        lca: TreeNode = root

        while asc_p and asc_q:
            if asc_p[0].val != asc_q[0].val:
                break

            lca = asc_p.popleft()
            asc_q.popleft()

        return lca
