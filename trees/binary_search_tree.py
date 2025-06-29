from __future__ import annotations
from collections import deque
from typing import Optional

CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"


class BSTNode:
    def from_list(values: list[int | None] = []) -> BSTNode | None:
        if len(values) == 0:
            return None
        queue = deque(values)
        value = queue.popleft()
        root = BSTNode(value)

        while queue:
            value = queue.popleft()
            if value is None:
                continue
            root = BSTNode.insert(root=root, key=value)

        return root

    @staticmethod
    def display_v1(node: BSTNode, prefix="", is_left=True) -> str:
        if not node or node.length == 0:
            return ""

        result = ""

        if node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            result += BSTNode.display_v1(node.right, new_prefix, False)
        result += prefix
        if prefix:
            result += "└── " if is_left else "┌── "

        result += f"{node.val}.{node.height}.{RESET}\n"

        if node.left:
            new_prefix = prefix + ("    " if is_left else "│   ")
            result += BSTNode.display_v1(node.left, new_prefix, True)
        return result

    def __init__(self, val: int, left: Optional[BSTNode] = None, right: Optional[BSTNode] = None):
        """Initialize an AVL tree node."""
        self.val = val
        self.left = left
        self.right = right
        self.length = 1
        self.height = 1

    def __repr__(self):
        return BSTNode.display_v1(self).rstrip()

    def contains(self, target: int) -> bool:
        if not self or self.length == 0:
            return False

        if self.val == target:
            return True

        left = self.left.contains(target=target) if self.left else False
        right = self.right.contains(target=target) if self.right else False

        return left or right

    def binary_search(self, target: int) -> tuple[BSTNode | None, BSTNode | None]:
        """Binary search to find a target value."""
        if not self:
            return False

        node = self
        parent = None
        while node:
            if node.val == target:
                return node, parent
            elif target < node.val:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        return node, parent

    def max(self) -> tuple[BSTNode | None, BSTNode | None]:
        """Find the maximum value in the AVL tree."""
        parent = None
        node = self
        while node and node.right:
            parent = node
            node = node.right
        return node, parent

    def min(self) -> tuple[BSTNode | None, BSTNode | None]:
        """Find the minimum value in the AVL tree."""
        parent = None
        node = self
        while node and node.left:
            parent = node
            node = node.left
        return node, parent

    def swap_child(self, child: BSTNode, target: BSTNode | None) -> None:
        """Swap a child node from the AVL tree."""
        if self.left == child:
            self.left = target
        elif self.right == child:
            self.right = target
        # else:
        #     raise ValueError("Child node not found in this BSTNode.")

    def _delete_root(self) -> None:
        """Delete the root node of the AVL tree."""
        if not self.left and not self.right:
            self.length = 0
            self.height = 0
            return None

        if not self.left:
            temp = self.right
            self.right = temp.right
            temp.right = None
            self.left = temp.left
            temp.left = None
            self.val = temp.val
        elif not self.right:
            temp = self.left
            self.left = temp.left
            temp.left = None
            self.right = temp.right
            temp.right = None
            self.val = temp.val
        else:
            max_subnode, max_subnode_parent = self.left.max()
            if max_subnode is self.left:
                self.val = max_subnode.val
                self.left = max_subnode.left
                max_subnode.left = None

            if max_subnode_parent:
                max_subnode_parent.right = max_subnode.left

            self.val = max_subnode.val

    @staticmethod
    def delete(root: BSTNode, key: int) -> BSTNode | None:
        """Delete a key from the BST tree."""
        node, parent = root.binary_search(target=key)
        if not node:
            return root

        if not parent:
            root._delete_root()
            return root

        if not node.left and not node.right:
            parent.swap_child(child=node, target=None)

        elif node.left and not node.right:
            parent.swap_child(child=node, target=node.left)
            node.left = None

        elif node.right and not node.left:
            parent.swap_child(child=node, target=node.right)
            node.right = None

        else:
            max_subnode, max_subnode_parent = node.left.max()
            if max_subnode_parent:
                max_subnode_parent.right = max_subnode.left

            if max_subnode is not node.left:
                max_subnode.left = node.left

            max_subnode.right = node.right

            parent.swap_child(child=node, target=max_subnode)

        node.left = None
        node.right = None

        return root

    @staticmethod
    def insert(root: BSTNode, key: int) -> BSTNode:
        """Insert a new key into the binary search tree."""
        node: BSTNode | None = root
        parent: BSTNode | None = None
        while node:
            if key == node.val:
                break
            elif key < node.val:
                parent = node
                node = node.left
            elif key > node.val:
                parent = node
                node = node.right

        if node and key == node.val:
            return root
        if key < parent.val:
            parent.left = BSTNode(key)
        elif key > parent.val:
            parent.right = BSTNode(key)
        return root
