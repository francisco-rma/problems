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

import time
from lca_bst import TreeNode

# Benchmark for creating a large BST

start_time = time.time()

# root = TreeNode.from_list([5, 3, 8, 1, 4, 7, 9, None, 2])
root = TreeNode.create_large_bst(2000000)
p = TreeNode.seek(root, target=100000)
q = TreeNode.seek(root, target=1000000)

end_time = time.time()

print(
    f"Bounds:\n {max([p.val,q.val])} - {min([p.val,q.val])} \nTree creation time: {end_time - start_time:.6f} seconds"
)


# Benchmark for lowestCommonAncestor
start_time = time.time()
result_lca = TreeNode.lowestCommonAncestor(root=root, p=p, q=q)
end_time = time.time()
print(
    f"lowestCommonAncestor result:\n {result_lca.val} \nTime: {end_time - start_time:.6f} seconds"
)

# Benchmark for lowestCommonAncestorControl
start_time = time.time()
result_lca_control = TreeNode.lowestCommonAncestorNaive(root=root, p=p, q=q)
end_time = time.time()
print(
    f"lowestCommonAncestorControl result:\n {result_lca_control.val} \nTime: {end_time - start_time:.6f} seconds"
)

# Benchmark for lowestCommonAncestorControlV2
start_time = time.time()
result_lca_control = TreeNode.lowestCommonAncestor(root=root, p=p, q=q)
end_time = time.time()
print(
    f"lowestCommonAncestorControlV2 result:\n {result_lca_control.val} \nTime: {end_time - start_time:.6f} seconds"
)

# =======================================================
# =======================================================
