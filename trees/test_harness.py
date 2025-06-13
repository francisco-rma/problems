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
import numpy as np
from avl_tree import AVLNode
from valid_bst import isValidBST

population = random.sample(range(1000), k=10)
root: AVLNode = AVLNode.from_list(population)
print(root)

target = 500
result = root.contains(target=target)

print(f"Search result for target {target}: {result}")

target = population[len(population) // 2]
result = root.contains(target=target)
print(f"Search result for target {target}: {result}")


def test_insertion():
    rng = np.random.default_rng(42)  # Seed for reproducibility

    source = [9, 3, 20, None, None, 15, 25]
    my_tree: AVLNode = AVLNode.from_list(source)

    assert my_tree and isValidBST(my_tree)

    for index in range(100):
        insertion_target = rng.integers(low=0, high=1000, size=1)[0]

        (result, parent) = my_tree.insert(key=insertion_target)

        assert isValidBST(my_tree)
        assert parent is not None
        assert result is not None
        assert result.val == insertion_target

        assert my_tree.contains(
            target=insertion_target
        ), f"Target {insertion_target} not found in the tree after insertion."

        node, parent = my_tree.binary_search(target=insertion_target)
        assert node is not None and node.val == insertion_target

        print("------------------------" + f"Iteration ${index} " + "------------------------")
        print("Insertion target:", insertion_target)
        print("Result node:", result)
        print("Parent node:", parent)
        print("\n")

    print("Result tree:\n")
    print(my_tree)


test_insertion()

# =======================================================
# =======================================================
