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
        def display(node: AVLNode, prefix="", is_left=True) -> str:
            if not node or node.length == 0:
                return f"{RESET}"

            result = f"{BOLD}"

            if node.right:
                new_prefix = prefix + ("│   " if is_left else "    ")
                result += display(node.right, new_prefix, False)
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
            result += f"{node.val}{RESET}\n"

            if node.left:
                new_prefix = prefix + ("    " if is_left else "│   ")
                result += display(node.left, new_prefix, True)
            return result

        return display(self).rstrip()

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

    def update_heights(self) -> None:
        if not self:
            return

        if self.left:
            self.left.update_heights()
        if self.right:
            self.right.update_heights()

        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)
        return

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
            root.update_heights()
        elif key > parent.val:
            parent.right = AVLNode(key)
            root.update_heights()
        return root

    def swap_child(self, child: AVLNode, target: AVLNode | None) -> None:
        """Prune a child node from the AVL tree."""
        if self.left == child:
            self.left = target
        elif self.right == child:
            self.right = target
        # else:
        #     raise ValueError("Child node not found in this AVLNode.")

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
        self.length -= 1
        self.update_heights()

    @staticmethod
    def delete(root: AVLNode, key: int) -> AVLNode | None:
        """Delete a key from the AVL tree."""
        if not root:
            return None

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

        print(root)
        node.left = None
        node.right = None
        root.length -= 1
        root.update_heights()
        return root

    def _left_rotate(root: AVLNode) -> AVLNode:
        """Perform a left rotation on the AVL tree."""
        if not root.right:
            return root
        pivot = root.right

        root.right = pivot.left
        pivot.left = root
        root = pivot
        root.update_heights()
        return root

    def _right_rotate(root: AVLNode) -> AVLNode:
        """Perform a left rotation on the AVL tree."""
        if not root.left:
            return root
        pivot = root.left

        root.left = pivot.right
        pivot.right = root
        root = pivot
        root.update_heights()
        return root

    def avl_walk(node: AVLNode | None) -> AVLNode | None:
        if not node:
            return None

        # AVLNode.avl_transform(node=node)

        if node.left:
            AVLNode.avl_walk(node.left)

        # AVLNode.avl_transform(node=node)

        if node.right:
            AVLNode.avl_walk(node.right)

        node = AVLNode.avl_transform(node=node)
        return node

    def avl_transform(node: AVLNode) -> AVLNode | None:
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
                print("right heavy or balanced right child")
                node = AVLNode._left_rotate(node)
            # left heavy right child
            else:
                print("left heavy right child")
                node.right = AVLNode._right_rotate(node.right)
                node = AVLNode._left_rotate(node)

        return node

    def avl_check(node: AVLNode | None) -> tuple[bool, int]:
        if not node:
            return True, -1

        left_check, left_height = AVLNode.avl_check(node.left)
        right_check, right_height = AVLNode.avl_check(node.right)
        balance = right_height - left_height

        is_avl = -1 <= balance <= 1 and left_check and right_check
        height = 1 + max(left_height, right_height)

        return is_avl, height
