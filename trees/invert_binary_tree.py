from binary_tree import Node, generate_root, populate_binary_tree

MAX_LVL = 3


def invert_bst(root: Node) -> Node:
    if root.left == root.right == None:
        return
    root.left, root.right = root.right, root.left
    invert_bst(root.left)
    invert_bst(root.right)
    return root


values = [4, 2, 7, 1, 3, 6, 9]
values = [1, 2]
values = [2, 3, None, 1]

binary_tree_test = Node(4)
binary_tree_test.left = Node(2)
binary_tree_test.right = Node(7)
binary_tree_test.left.left = Node(1)
binary_tree_test.left.right = Node(3)
binary_tree_test.right.left = Node(6)
binary_tree_test.right.right = Node(9)

tree = populate_binary_tree(values=values)
inverted_tree = populate_binary_tree(values=values, inverted=True)

root = generate_root(tree)
inverted_root = generate_root(inverted_tree)
inverted_root_test = generate_root(tree, inverted=True)
inverted_tree_test = populate_binary_tree(inverted_root)

assert inverted_root == inverted_root_test
assert inverted_tree_test == inverted_tree


validation1 = tree == binary_tree_test
validation2 = inverted_root == [4, 7, 2, 9, 6, 3, 1]
validation3 = inverted_tree == inverted_tree_test

print(f"Validation 1: {validation1}")
print(f"Validation 2: {validation2}")
print(f"Validation 3: {validation3}")
