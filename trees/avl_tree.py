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


class AVLNode:
    @staticmethod
    def display_v1(node: AVLNode, prefix="", is_left=True) -> str:
        if not node or node.length == 0:
            return f"{RESET}"

        result = f"{BOLD}"

        if node.right:
            new_prefix = prefix + ("│   " if is_left else "    ")
            result += AVLNode.display_v1(node.right, new_prefix, False)
        result += prefix
        if prefix:
            result += "└── " if is_left else "┌── "

        balance = node.balance()
        if balance == -1:
            result += f"{YELLOW}"
        elif balance == 0:
            result += f"{GREEN}"
        elif balance == 1:
            result += f"{BLUE}"
        else:
            result += f"{RED}"
        result += f"{node.val}.{node.height}.{RESET}\n"

        if node.left:
            new_prefix = prefix + ("    " if is_left else "│   ")
            result += AVLNode.display_v1(node.left, new_prefix, True)
        return result

    def from_list(values: list[int | None]) -> AVLNode | None:
        if not values:
            return None
        queue = deque(values)
        value = queue.popleft()
        root = AVLNode(value)

        while queue:
            value = queue.popleft()
            if value is None:
                continue
            root = AVLNode.insert(root=root, key=value)

        return root

    def __init__(self, val: int, left: Optional[AVLNode] = None, right: Optional[AVLNode] = None):
        """Initialize an AVL tree node."""
        self.val = val
        self.left = left
        self.right = right
        self.length = 1
        self.height = 0

    def __repr__(self):
        return AVLNode.display_v1(self).rstrip()

    def bfs_traverse(self):
        queue: deque[tuple[AVLNode, int]] = deque([(self, 1)])

        while queue:
            node, level = queue.pop()
            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))
            yield node, level

    def dfs_pre_order_traverse(self):
        if not self:
            yield
        yield self.val
        if self.left:
            yield from self.left.dfs_pre_order_traverse()
        if self.right:
            yield from self.right.dfs_pre_order_traverse()

    def dfs_post_order_traverse(self):
        if not self:
            yield
        if self.left:
            yield from self.left.dfs_post_order_traverse()
        if self.right:
            yield from self.right.dfs_post_order_traverse()

        yield self.val

    def dfs_in_order_traverse(self):
        if not self:
            yield
        if self.left:
            yield from self.left.dfs_in_order_traverse()
        yield self.val
        if self.right:
            yield from self.right.dfs_in_order_traverse()

    def balance(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return right_height - left_height

    def contains(self, target: int) -> bool:
        if not self or self.length == 0:
            return False

        if self.val == target:
            return True

        left = self.left.contains(target=target) if self.left else False
        right = self.right.contains(target=target) if self.right else False

        return left or right

    def binary_search(self, target: int) -> tuple[AVLNode | None, AVLNode | None]:
        """Binary search to find a target value. Returns a tuple of (target, parent)"""
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

    def max(self) -> tuple[AVLNode | None, AVLNode | None]:
        """Find the maximum value in the AVL tree."""
        parent = None
        node = self
        while node and node.right:
            parent = node
            node = node.right
        return node, parent

    def min(self) -> tuple[AVLNode | None, AVLNode | None]:
        """Find the minimum value in the AVL tree."""
        parent = None
        node = self
        while node and node.left:
            parent = node
            node = node.left
        return node, parent

    def swap_child(self, child: AVLNode, target: AVLNode | None) -> None:
        """Prune a child node from the AVL tree."""
        if self.left == child:
            self.left = target
        elif self.right == child:
            self.right = target

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
            max_subnode.left = None
            self.val = max_subnode.val
        self.length -= 1
        AVLNode.update_stats(node=self)

    def is_avl(self):
        result, _ = AVLNode.avl_check(node=self)
        return result

    @staticmethod
    def update_stats(node: AVLNode | None) -> tuple[int, int] | None:
        if not node:
            return None

        left_height, left_length = AVLNode.update_stats(node=node.left) if node.left else (-1, 0)
        right_height, right_length = (
            AVLNode.update_stats(node=node.right) if node.right else (-1, 0)
        )

        node.height = 1 + max(left_height, right_height)
        node.length = 1 + left_length + right_length

        return node.height, node.length

    @staticmethod
    def bst_insert(root: AVLNode, key: int) -> AVLNode | None:
        """Insert a new key into the AVL tree."""
        node: AVLNode | None = root
        parent: AVLNode | None = None
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
            parent.left = AVLNode(key)
        elif key > parent.val:
            parent.right = AVLNode(key)
        AVLNode.update_stats(root)
        return root

    @staticmethod
    def insert(root: AVLNode, key: int) -> AVLNode:
        """Insert a new key into the AVL tree."""
        node: AVLNode | None = root
        parent: AVLNode | None = None
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

        root.length += 1

        if key < parent.val:
            parent.left = AVLNode(key)
        elif key > parent.val:
            parent.right = AVLNode(key)

        root = AVLNode.avl_transform(node=root)
        return root

    @staticmethod
    def delete(root: AVLNode, key: int) -> AVLNode | None:
        """Delete a key from the AVL tree."""
        if not root:
            return None

        node, parent = root.binary_search(target=key)

        if not node:
            return AVLNode.avl_transform(node=root)

        if not parent:
            root._delete_root()

            root = AVLNode.avl_transform(node=root)

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
        root.length -= 1

        root = AVLNode.avl_transform(node=root)
        return root

    @staticmethod
    def _left_rotate(root: AVLNode) -> AVLNode:
        """Perform a left rotation on the AVL tree."""
        if not root.right:
            return root
        pivot = root.right

        root.right = pivot.left
        pivot.left = root
        return pivot

    @staticmethod
    def _right_rotate(root: AVLNode) -> AVLNode:
        """Perform a left rotation on the AVL tree."""
        if not root.left:
            return root
        pivot = root.left

        root.left = pivot.right
        pivot.right = root
        return pivot

    @staticmethod
    def avl_walk(node: AVLNode | None) -> AVLNode | None:
        if not node:
            return None
        if node.left:
            AVLNode.avl_walk(node.left)
        if node.right:
            AVLNode.avl_walk(node.right)
        node = AVLNode.avl_transform(node=node)
        return node

    @staticmethod
    def avl_transform(node: AVLNode) -> AVLNode | None:
        if not node:
            return None

        node.left = AVLNode.avl_transform(node=node.left)
        node.right = AVLNode.avl_transform(node=node.right)
        balance = node.balance()

        # balanced node
        if -1 <= balance <= 1:
            pass

        # left heavy node
        elif balance < -1:
            assert node.left is not None
            left_balance = node.left.balance()

            # left heavy or balanced left child
            if left_balance <= 0:
                node = AVLNode._right_rotate(node)
            # right heavy left child
            else:
                node.left = AVLNode._left_rotate(node.left)
                node = AVLNode._right_rotate(node)

        # right heavy node
        elif balance > 1:
            assert node.right is not None
            right_balance = node.right.balance()

            # right heavy or balanced right child
            if right_balance >= 0:
                node = AVLNode._left_rotate(node)
            # left heavy right child
            else:
                node.right = AVLNode._right_rotate(node.right)
                node = AVLNode._left_rotate(node)

        AVLNode.update_stats(node=node)
        return node

    @staticmethod
    def avl_transform_and_validate(node: AVLNode) -> AVLNode | None:
        if not node:
            return None

        node.left = AVLNode.avl_transform_and_validate(node=node.left)
        node.right = AVLNode.avl_transform_and_validate(node=node.right)
        balance = node.balance()

        order = list(node.dfs_in_order_traverse())

        # balanced node
        if -1 <= balance <= 1:
            pass

        # left heavy node
        elif balance < -1:
            assert node.left is not None
            left_balance = node.left.balance()

            # left heavy or balanced left child
            if left_balance <= 0:
                node = AVLNode._right_rotate(node)
            # right heavy left child
            else:
                node.left = AVLNode._left_rotate(node.left)
                node = AVLNode._right_rotate(node)

        # right heavy node
        elif balance > 1:
            assert node.right is not None
            right_balance = node.right.balance()

            # right heavy or balanced right child
            if right_balance >= 0:
                node = AVLNode._left_rotate(node)
            # left heavy right child
            else:
                node.right = AVLNode._right_rotate(node.right)
                node = AVLNode._left_rotate(node)

        for idx, val in enumerate(node.dfs_in_order_traverse()):
            assert val == order[idx]

        AVLNode.update_stats(node=node)
        return node

    @staticmethod
    def avl_check(node: AVLNode | None) -> tuple[bool, int]:
        if not node:
            return True, -1

        left_check, left_height = AVLNode.avl_check(node.left)
        right_check, right_height = AVLNode.avl_check(node.right)
        balance = right_height - left_height

        is_avl = -1 <= balance <= 1 and left_check and right_check
        height = 1 + max(left_height, right_height)

        return is_avl, height
