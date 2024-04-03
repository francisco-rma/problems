from bst import Node, generate_root, populate_bst

MAX_LVL = 3


def invert_bst(root: Node) -> Node:
    if root.left == root.right == None:
        return
    root.left, root.right = root.right, root.left
    invert_bst(root.left)
    invert_bst(root.right)
    return root


values = [4, 2, 7, 1, 3, 6, 9]

testBst = Node(4)
testBst.left = Node(2)
testBst.right = Node(7)

testBst.left.left = Node(1)
testBst.left.right = Node(3)
testBst.right.left = Node(6)
testBst.right.right = Node(9)

tree = populate_bst(values=values)
inverted_tree = populate_bst(values=values, inverted=True)

root = generate_root(tree)
inverted_root = generate_root(inverted_tree)


validation1 = tree == testBst
validation2 = inverted_root == [4, 7, 2, 9, 6, 3, 1]

print(f"Validation 1: {validation1}")
print(f"Validation 2: {validation2}")
