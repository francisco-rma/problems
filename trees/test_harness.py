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


from collections import deque
import random
import numpy as np
from avl_tree import AVLNode
from valid_bst import isValidBST

TEST_SIZE = 1 * 10**3
population = random.sample(range(1000), k=10)
root: AVLNode = AVLNode.from_list(population)

target = 500
result = root.contains(target=target)


target = population[len(population) // 2]
result = root.contains(target=target)


def test_insertion():
    source = [9, 3, 20, None, None, 15, 25]
    rng = np.random.default_rng()
    my_tree: AVLNode = AVLNode.from_list(source)
    assert isValidBST(my_tree)

    try:
        assert my_tree.is_avl()
    except Exception:
        print(my_tree)
        raise

    if not my_tree:
        raise ValueError("Tree is empty, cannot perform insertion tests.")

    for index in range(TEST_SIZE):
        insertion_target = rng.integers(low=0, high=1000, size=1)[0]
        my_tree = AVLNode.insert(root=my_tree, key=insertion_target)
        result, parent = my_tree.binary_search(target=insertion_target)

        assert my_tree
        assert isValidBST(my_tree)
        assert my_tree.is_avl()

        assert result is not None
        assert result.val == insertion_target
        assert my_tree.contains(
            target=insertion_target
        ), f"Target {insertion_target} not found in the tree after insertion."

        node, parent = my_tree.binary_search(target=insertion_target)
        assert node is not None and node.val == insertion_target


def test_deletion():
    source = [0]
    rng = np.random.default_rng()
    my_tree: AVLNode = AVLNode.from_list(source)
    assert my_tree.length == 1
    inserted_values: list[int] = []

    for _ in range(TEST_SIZE):
        val = rng.integers(low=1, high=1000, size=1)[0]
        if my_tree.contains(val):
            continue
        length = my_tree.length
        my_tree = AVLNode.insert(root=my_tree, key=val)
        assert my_tree.length == length + 1
        inserted_values.append(val)
        assert isValidBST(my_tree)
        assert my_tree.is_avl()
        assert my_tree.contains(target=val)

    aux = my_tree.val
    my_tree = AVLNode.delete(root=my_tree, key=aux)
    assert not my_tree.contains(target=aux)
    assert isValidBST(my_tree)
    assert my_tree.is_avl()

    my_tree = AVLNode.insert(root=my_tree, key=aux)
    assert my_tree.contains(target=aux)
    assert isValidBST(my_tree)
    assert my_tree.is_avl()

    queue = deque(set(inserted_values))
    while queue:
        val = queue.pop()
        node, parent = my_tree.binary_search(target=val)
        assert node is not None and node.val == val

        my_tree = AVLNode.delete(root=my_tree, key=val)

        assert my_tree.is_avl()
        assert not my_tree.contains(target=val)
        assert isValidBST(my_tree)

        for item in queue:
            assert my_tree.contains(
                target=item
            ), f"Item {item} should still be in the tree after deletion of {val}."


test_insertion()
test_deletion()

# =======================================================
# =======================================================
