from binary_tree import Node, populate_binary_tree

MAX_LVL = 3


def invert_bst(root: Node) -> Node:
    if root.left == root.right == None:
        return
    root.left, root.right = root.right, root.left
    invert_bst(root.left)
    invert_bst(root.right)
    return root


values = [4, 2, 7, 1, 3, 6, 9]
# values = [1, 2]
# values = [2, 3, None, 1]

binary_tree_test = Node(4)
binary_tree_test.left = Node(2)
binary_tree_test.right = Node(7)
binary_tree_test.left.left = Node(1)
binary_tree_test.left.right = Node(3)
binary_tree_test.right.left = Node(6)
binary_tree_test.right.right = Node(9)

inverted_tree = populate_binary_tree(values=values, inverted=True)

tree = populate_binary_tree(values=values)
tree.__invert__(tree)
assert tree == inverted_tree

tree = populate_binary_tree(values=values)
# tree.__invert_bfs__()

assert tree == inverted_tree
