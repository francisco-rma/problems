# =======================================================
# Test harness
# =======================================================


# =======================================================
# Same Tree
# =======================================================

from same_tree import TreeNode, isSameTree

p = [1, 2, 3]
q = [1, 2, 3]

p_root = TreeNode.from_list(p)
q_root = TreeNode.from_list(q)

# print(repr(p_root))
# print(repr(q_root))

assert TreeNode.generate_root(p_root) == p
assert TreeNode.generate_root(q_root) == q

result = isSameTree(p=p_root, q=q_root)

print(result)

# =======================================================
# =======================================================
