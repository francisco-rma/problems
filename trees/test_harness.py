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

# import time
# from lca_bst import TreeNode

# # Benchmark for creating a large BST

# start_time = time.time()

# # root = TreeNode.from_list([5, 3, 8, 1, 4, 7, 9, None, 2])
# root = TreeNode.create_large_bst(2000000)
# p = TreeNode.seek(root, target=100000)
# q = TreeNode.seek(root, target=1000000)

# end_time = time.time()

# print(
#     f"Bounds:\n {max([p.val,q.val])} - {min([p.val,q.val])} \nTree creation time: {end_time - start_time:.6f} seconds"
# )


# # Benchmark for lowestCommonAncestor
# start_time = time.time()
# result_lca = TreeNode.lowestCommonAncestor(root=root, p=p, q=q)
# end_time = time.time()
# print(
#     f"lowestCommonAncestor result:\n {result_lca.val} \nTime: {end_time - start_time:.6f} seconds"
# )

# # Benchmark for lowestCommonAncestorControl
# start_time = time.time()
# result_lca_control = TreeNode.lowestCommonAncestorNaive(root=root, p=p, q=q)
# end_time = time.time()
# print(
#     f"lowestCommonAncestorControl result:\n {result_lca_control.val} \nTime: {end_time - start_time:.6f} seconds"
# )

# # Benchmark for lowestCommonAncestorControlV2
# start_time = time.time()
# result_lca_control = TreeNode.lowestCommonAncestor(root=root, p=p, q=q)
# end_time = time.time()
# print(
#     f"lowestCommonAncestorControlV2 result:\n {result_lca_control.val} \nTime: {end_time - start_time:.6f} seconds"
# )

# =======================================================
# =======================================================


# =======================================================
# Level order traversal
# =======================================================


# import random
# from bt_level_order_traversal import TreeNode

# root: TreeNode = TreeNode.from_list(random.sample(range(1000), k=10))
# print(root)


# result = root.levelOrder(root=root)
# print(result)


# =======================================================
# =======================================================

# =======================================================
# AVL tree
# =======================================================


import random
from avl_tree import AVLNode
from valid_bst import isValidBST

TEST_SIZE = 1 * 10**2
POPULATION_SIZE = 1 * 10**2
population = range(POPULATION_SIZE * 10)

sample = random.sample(population=population, k=POPULATION_SIZE)
root: AVLNode = AVLNode.from_list(sample)
assert isValidBST(root=root)
assert root.is_avl()

print(root)

print("--------------dfs_pre_order_traverse--------------:")
for dfs_idx, val in enumerate(root.dfs_pre_order_traverse()):
    assert root.contains(val)
    print(f"DFS-{dfs_idx}: root contains value {val}")
print("\n")

print("--------------dfs_in_order_traverse--------------:")
for dfs_idx, val in enumerate(root.dfs_in_order_traverse()):
    assert root.contains(val)
    print(f"DFS-{dfs_idx}: root contains value {val}")
print("\n")

print("--------------dfs_post_order_traverse--------------:")
for dfs_idx, val in enumerate(root.dfs_post_order_traverse()):
    assert root.contains(val)
    print(f"DFS-{dfs_idx}: root contains value {val}")
print("\n")
for bfs_idx, (node, level) in enumerate(root.bfs_traverse()):
    assert root.contains(node.val)
    print(f"BFS-{bfs_idx}: root contains node {node.val} @ level {level}")

# =======================================================
# =======================================================
