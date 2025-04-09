# =======================================================
# Test harness
# =======================================================


# =======================================================
# Same Tree
# =======================================================

# from same_tree import TreeNode, isSameTree

# p = [1, 2, 3]
# q = [1, 2, 3]

# p_root = TreeNode.from_list(p)
# q_root = TreeNode.from_list(q)

# # print(repr(p_root))
# # print(repr(q_root))

# assert TreeNode.generate_root(p_root) == p
# assert TreeNode.generate_root(q_root) == q

# result = isSameTree(p=p_root, q=q_root)

# print(result)

# =======================================================
# =======================================================


# =======================================================
# Lowest common ancestor on binary search tree
# =======================================================

from lca_bst import TreeNode

root = TreeNode.from_list([5, 3, 8, 1, 4, 7, 9, None, 2])
p = TreeNode.seek(root, target=3)
q = TreeNode.seek(root, target=4)

print(repr(root))

# assert TreeNode.generate_root(p_root) == p
# assert TreeNode.generate_root(q_root) == q

result = TreeNode.lowestCommonAncestor(root=root, p=p, q=q)

print(result)

# =======================================================
# =======================================================
