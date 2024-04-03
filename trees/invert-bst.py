from typing import Sequence
from bst import Node

MAX_LVL = 3


def invert_bst(root: Node) -> Node | None:
    if root.left == root.right == None:
        return
    root.left, root.right = root.right, root.left
    invert_bst(root.left)
    invert_bst(root.right)
    return root


def populate_bst(values: Sequence[int]) -> Node:
    n = len(values)

    if n == 0:
        return None

    def inner(index: int = 0):
        if index >= n or values[index] is None:
            return None

        node = Node(values[index])

        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)

        return node

    return inner()


values = [4, 2, 7, 1, 3, 6, 9]

testBst = Node(4)
testBst.left = Node(2)
testBst.right = Node(7)

testBst.left.left = Node(1)
testBst.left.right = Node(3)
testBst.right.left = Node(6)
testBst.right.right = Node(9)

tree = populate_bst(values=values)

print(tree)
