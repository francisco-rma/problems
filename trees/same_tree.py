from __future__ import annotations
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

    def generate_root(tree: TreeNode, inverted=False) -> list[int]:
        root = []
        if tree is None:
            return root
        root.append(tree.val)

        def inner(node: TreeNode):
            if node is None:
                return
            has_left_node = node.left is not None
            has_right_node = node.right is not None

            left_val = node.left.val if has_left_node else None
            right_val = node.right.val if has_right_node else None

            if has_left_node and has_right_node:
                root.append(left_val if not inverted else right_val)
                root.append(right_val if not inverted else left_val)
                inner(node.left) if not inverted else inner(node.right)
                inner(node.right) if not inverted else inner(node.left)

            elif has_left_node:
                if inverted:
                    root.append(right_val)
                root.append(left_val)

            elif has_right_node:
                if not inverted:
                    root.append(left_val)
                root.append(right_val)

        inner(tree)

        return root


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def is_equivalent(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return q is None
        elif not q:
            return p is None

        left = is_equivalent(p.left, q.left)
        right = is_equivalent(p.right, q.right)

        return left and right and p.val == q.val

    result = is_equivalent(p, q)

    return result
