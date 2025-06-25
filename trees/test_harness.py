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


import time
from collections import deque
import random

import numpy as np
from avl_tree import AVLNode
from binary_search_tree import BSTNode
from valid_bst import isValidBST
import cProfile


TEST_SIZE = 10**3
N = 1 * 10**6


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def bst_benchmark():
    print("\n[ BST BENCHMARK ]")
    population = range(1, N * 10)

    values = random.sample(population=population, k=N)
    root = BSTNode(0)

    # Insert
    t0 = time.time()
    for v in values:
        root = BSTNode.insert(root=root, key=v)
    t1 = time.time()
    print(f"BST insert {N} values: {t1-t0:.4f}s")

    # In-order traversal
    def in_order(node: BSTNode):
        if not node:
            return []
        return in_order(node.left) + [node.val] + in_order(node.right)

    t0 = time.time()
    order = in_order(root)
    t1 = time.time()
    print(f"BST in-order traversal: {t1-t0:.4f}s, sorted: {order == sorted(set(order))}")

    # Search
    t0 = time.time()
    for v in values:
        _, _ = root.binary_search(target=v)
    t1 = time.time()
    print(f"BST full search: {t1-t0:.4f}s")

    # Delete
    random.shuffle(values)
    t0 = time.time()
    for v in values:
        root = BSTNode.delete(root, v)
    t1 = time.time()
    print(f"BST delete {N} values: {t1-t0:.4f}s")
    print("BST benchmark complete.\n")


def avl_bst_benchmark():
    print("\n[ AVL BENCHMARK ]")
    population = range(1, N * 10)

    values = random.sample(population=population, k=N)
    root = AVLNode(0)

    # Insert
    t0 = time.time()
    for v in values:
        _, root = AVLNode.rinsert(root=root, key=v)
    t1 = time.time()
    print(f"AVL insert {N} values: {t1-t0:.4f}s")

    # In-order traversal
    def in_order(node: AVLNode):
        if not node:
            return []
        return in_order(node.left) + [node.val] + in_order(node.right)

    t0 = time.time()
    order = in_order(root)
    t1 = time.time()
    print(f"AVL in-order traversal: {t1-t0:.4f}s, sorted: {order == sorted(set(order))}")

    # Search
    t0 = time.time()
    for v in values:
        _, _ = root.binary_search(target=v)
    t1 = time.time()
    print(f"AVL full search: {t1-t0:.4f}s")

    # Delete
    random.shuffle(values)
    t0 = time.time()
    for v in values:
        root = AVLNode.delete(root, v)
    t1 = time.time()
    print(f"AVL delete {N} values: {t1-t0:.4f}s")
    print("AVL benchmark complete.\n")


def generate_samples() -> tuple[AVLNode, AVLNode]:
    print("Setting up...")
    population = range(N * 10)
    sample = random.sample(population=population, k=N)

    queue = deque(sample)
    value = queue.popleft()
    root = AVLNode(value)
    avl_root = AVLNode(value)
    assert id(root) != id(avl_root)

    while queue:
        value = queue.popleft()
        if value is None:
            continue
        root = AVLNode.bst_insert(root=root, key=value)
        avl_root = AVLNode.insert(root=avl_root, key=value)

    print("ASSERTIONS")

    assert isValidBST(root=root)
    print("TEST - isValidBST: ✅")

    assert isValidBST(root=avl_root)
    print("CONTROL - isValidBST: ✅")

    assert not root.is_avl()
    print("TEST - is_avl: ❌")

    assert avl_root.is_avl()
    print("CONTROL - is_avl: ✅")

    test_order = list(root.dfs_in_order_traverse())
    assert is_sorted(test_order)
    print("TEST - in_order_traverse sorted: ✅")

    control_order = list(avl_root.dfs_in_order_traverse())
    assert is_sorted(control_order)
    print("CONTROL - in_order_traverse sorted: ✅")

    return root, avl_root


cProfile.run("bst_benchmark()")
cProfile.run("avl_bst_benchmark()")

# =======================================================
# =======================================================
