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


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def bst_benchmark(root):
    print("\n[ BST BENCHMARK ]")
    N = 10_000
    values = list(range(N))
    random.shuffle(values)
    # Insert
    t0 = time.time()
    for v in values:
        root = BSTNode.insert(root, v)
    t1 = time.time()
    print(f"BST insert {N} values: {t1-t0:.4f}s")

    # In-order traversal
    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node.val] + in_order(node.right)

    t0 = time.time()
    order = in_order(root)
    t1 = time.time()
    print(f"BST in-order traversal: {t1-t0:.4f}s, sorted: {order == sorted(set(order))}")
    # # Delete
    random.shuffle(values)
    t0 = time.time()
    for i, v in enumerate(values):
        root = BSTNode.delete(root, v)
    t1 = time.time()
    print(f"BST delete {N} values: {t1-t0:.4f}s")
    print("BST benchmark complete.\n")


def avl_bst_benchmark(root):
    print("\n[ AVL BENCHMARK ]")
    N = 10_000
    values = list(range(N))
    random.shuffle(values)
    # Insert
    t0 = time.time()
    for i, v in enumerate(values):
        # root = AVLNode.insert(root=root, key=v)
        _, root = AVLNode.rinsert(root=root, key=v)
        # t0 = time.time()
        # t1 = time.time()
        # print(f"duration: {t1-t0} - length: {root.length}")
    t1 = time.time()
    print(f"AVL insert {N} values: {t1-t0:.4f}s")

    # In-order traversal
    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node.val] + in_order(node.right)

    t0 = time.time()
    order = in_order(root)
    t1 = time.time()
    print(f"AVL in-order traversal: {t1-t0:.4f}s, sorted: {order == sorted(set(order))}")
    # # Delete
    random.shuffle(values)
    t0 = time.time()
    for v in values:
        root = AVLNode.delete(root, v)
    t1 = time.time()
    print(f"AVL delete {N} values: {t1-t0:.4f}s")
    print("AVL benchmark complete.\n")


def generate_samples() -> tuple[AVLNode, AVLNode]:
    POPULATION_SIZE = 1 * 10**2
    population = range(POPULATION_SIZE * 10)
    sample = random.sample(population=population, k=POPULATION_SIZE)

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

    assert isValidBST(root=root)
    assert isValidBST(root=avl_root)
    assert avl_root.is_avl()
    control_order = list(avl_root.dfs_in_order_traverse())
    assert is_sorted(control_order)

    print(f"root (AVL {root.is_avl()}:\n{root}\n")
    print(f"control_root (AVL {avl_root.is_avl()}:\n{avl_root}\n")

    return root, avl_root


def test_recursive_insertion():
    source = [9, 3, 20, None, None, 15, 25]
    rng = np.random.default_rng(100)
    # rng = np.random.default_rng()
    my_tree: AVLNode = AVLNode.from_list(source)
    assert isValidBST(my_tree)

    assert my_tree.is_avl()

    if not my_tree:
        raise ValueError("Tree is empty, cannot perform insertion tests.")

    for index in range(10**1):
        insertion_target = rng.integers(low=0, high=1000, size=1)[0]
        print(f"Insertion target: {insertion_target}")
        print(f"Before: \n{my_tree}")
        start = time.time()
        inserted, my_tree = AVLNode.rinsert(root=my_tree, key=insertion_target)
        print(f"duration: {time.time()-start} - length: {my_tree.length}")
        print(f"inserted: {inserted}")
        print(f"After: \n{my_tree}")

        assert isValidBST(my_tree)
        assert my_tree.is_avl()
        assert my_tree.height >= 1
        assert my_tree.contains(
            target=insertion_target
        ), f"Target {insertion_target} not found in the tree after insertion."

        node, parent = my_tree.binary_search(target=insertion_target)
        assert node is not None and node.val == insertion_target

    # print(my_tree)


# test_recursive_insertion()

root, avl_root = generate_samples()

cProfile.run("bst_benchmark(root=root)")
cProfile.run("avl_bst_benchmark(root=avl_root)")

# =======================================================
# =======================================================
