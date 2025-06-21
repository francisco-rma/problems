from collections import deque
import random
import numpy as np
from trees.avl_tree import AVLNode
from trees.valid_bst import isValidBST

TEST_SIZE = 1 * 10**3


def test_left_rotate_root():
    root = AVLNode(17)
    root.left = AVLNode(9)
    root.right = AVLNode(50)
    root.right.left = AVLNode(23)
    root.right.right = AVLNode(76)
    AVLNode.update_stats(node=root)

    assert isValidBST(root)
    root = AVLNode._left_rotate(root)
    assert isValidBST(root)

    assert root.val == 50
    assert root.left is not None and root.left.val == 17
    assert root.right is not None and root.right.val == 76
    assert root.left.right is not None and root.left.right.val == 23
    assert root.left.left is not None and root.left.left.val == 9


def test_left_rotate_nonroot():
    root = AVLNode(17)
    root.left = AVLNode(9)
    root.right = AVLNode(50)
    root.right.left = AVLNode(23)
    root.right.right = AVLNode(76)
    AVLNode.update_stats(node=root)

    assert isValidBST(root)
    root.right = AVLNode._left_rotate(root.right)
    assert isValidBST(root)

    assert root.val == 17
    assert root.left is not None and root.left.val == 9
    assert root.right is not None and root.right.val == 76
    assert root.right.left is not None and root.right.left.val == 50
    assert root.right.left.left is not None and root.right.left.left.val == 23


def test_right_rotate_root():
    root = AVLNode(50)
    root.left = AVLNode(17)
    root.right = AVLNode(76)
    root.left.left = AVLNode(9)
    root.left.right = AVLNode(23)
    AVLNode.update_stats(node=root)

    assert isValidBST(root)
    print(root.val)
    root = AVLNode._right_rotate(root)
    print(root.val)
    assert isValidBST(root)

    assert root.val == 17
    assert root.left is not None and root.left.val == 9
    assert root.right is not None and root.right.val == 50
    assert root.right.left is not None and root.right.left.val == 23
    assert root.right.right is not None and root.right.right.val == 76


def test_right_rotate_nonroot():
    root = AVLNode(50)
    root.left = AVLNode(17)
    root.right = AVLNode(76)
    root.left.left = AVLNode(9)
    root.left.right = AVLNode(23)
    AVLNode.update_stats(node=root)

    assert isValidBST(root)
    root.left = AVLNode._right_rotate(root.left)
    assert isValidBST(root)

    assert root.val == 50
    assert root.left is not None and root.left.val == 9
    assert root.right is not None and root.right.val == 76
    assert root.left.left is None
    assert root.left.right is not None and root.left.right.val == 17
    assert root.left.right.right is not None and root.left.right.right.val == 23


def test_avl_walk_lh1():
    root = AVLNode(50)
    root.left = AVLNode(17)
    root.right = AVLNode(76)
    root.left.left = AVLNode(9)
    root.left.right = AVLNode(23)
    root.left.right.left = AVLNode(20)
    AVLNode.update_stats(node=root)
    print(root)

    assert isValidBST(root)
    root = AVLNode.avl_walk(root)
    assert AVLNode.avl_check(root)
    assert isValidBST(root)


def test_avl_walk_lh2():
    root = AVLNode(50)
    root.left = AVLNode(17)
    root.right = AVLNode(76)
    root.left.left = AVLNode(9)
    root.left.right = AVLNode(23)
    root.left.left.right = AVLNode(11)
    AVLNode.update_stats(node=root)
    print(root)

    assert isValidBST(root)
    root = AVLNode.avl_walk(root)
    assert AVLNode.avl_check(root)
    assert isValidBST(root)
    print(root)


def test_avl_walk_rh1():
    root = AVLNode(50)
    root.left = AVLNode(17)
    root.right = AVLNode(76)
    root.right.left = AVLNode(60)
    root.right.right = AVLNode(100)
    root.right.left.right = AVLNode(70)
    AVLNode.update_stats(node=root)
    print(root)

    assert isValidBST(root)
    root = AVLNode.avl_walk(root)
    print(root)
    assert AVLNode.avl_check(root)
    assert isValidBST(root)


def test_avl_walk_rh2():
    root = AVLNode(50)
    root.left = AVLNode(17)
    root.right = AVLNode(76)
    root.right.left = AVLNode(60)
    root.right.right = AVLNode(100)
    root.right.right.right = AVLNode(155)
    AVLNode.update_stats(node=root)
    print(root)

    assert isValidBST(root)
    root = AVLNode.avl_walk(root)
    print(root)
    assert AVLNode.avl_check(root)
    assert isValidBST(root)


def test_avl_check_and_height_consistency():
    # Build a tree
    source = [17, 9, 50, 23, 76, 5, 12, 30, 60]
    root: AVLNode = AVLNode.from_list(source)
    assert root.is_avl()
    # AVLNode.update_stats(node=root)

    # Use avl_check to get organic heights
    is_avl, organic_height = AVLNode.avl_check(root)
    assert is_avl, "Tree should satisfy AVL property"

    # Compare organic height with stored property
    assert (
        root.height == organic_height
    ), f"Stored height {root.height} != organic height {organic_height}"

    # Recursively compare all node heights
    def compare_heights(node: AVLNode | None):
        if not node:
            return -1
        is_avl, organic = AVLNode.avl_check(node)
        assert is_avl, f"Subtree rooted at {node.val} is not AVL"
        assert (
            node.height == organic
        ), f"Node {node.val}: stored height {node.height} != organic {organic}"
        compare_heights(node.left)
        compare_heights(node.right)

    compare_heights(root)


def test_insertion():
    source = [9, 3, 20, None, None, 15, 25]
    # rng = np.random.default_rng(100)
    rng = np.random.default_rng()
    my_tree: AVLNode = AVLNode.from_list(source)
    assert isValidBST(my_tree)

    assert my_tree.is_avl()

    if not my_tree:
        raise ValueError("Tree is empty, cannot perform insertion tests.")

    for index in range(TEST_SIZE):
        insertion_target = rng.integers(low=0, high=1000, size=1)[0]
        print(f"Insertion target: {insertion_target}")
        print(f"Before: \n{my_tree}")
        my_tree = AVLNode.insert(root=my_tree, key=insertion_target)
        print(f"After: \n{my_tree}")
        result, parent = my_tree.binary_search(target=insertion_target)

        assert my_tree
        assert isValidBST(my_tree)
        assert my_tree.is_avl()
        assert my_tree.height >= 1
        assert result is not None
        assert result.val == insertion_target
        assert my_tree.contains(
            target=insertion_target
        ), f"Target {insertion_target} not found in the tree after insertion."

        node, parent = my_tree.binary_search(target=insertion_target)
        assert node is not None and node.val == insertion_target

    print(my_tree)


def test_deletion():
    source = [0]
    # rng = np.random.default_rng(100)
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

        assert isValidBST(my_tree)
        assert my_tree.is_avl()

        for item in queue:
            assert my_tree.contains(
                target=item
            ), f"Item {item} should still be in the tree after deletion of {val}."
        assert not my_tree.contains(target=val)


def test_from_list():
    rng = np.random.default_rng()
    source = rng.integers(low=1, high=1000, size=TEST_SIZE).tolist()

    my_tree: AVLNode = AVLNode.from_list(source)
    assert isValidBST(my_tree)
    assert my_tree.is_avl()

    for val in source:
        assert my_tree.contains(target=val), f"Value {val} should be in the tree."


def test_height():
    source = [9, 3, 20, None, None, 15, 25]
    my_tree: AVLNode = AVLNode.from_list(source)
    assert isValidBST(my_tree)
    assert my_tree.is_avl()

    print(my_tree.height)
    print(my_tree)
    assert my_tree.height == 2, f"Expected height 2, got {my_tree.height}"

    my_tree = AVLNode.insert(root=my_tree, key=10)
    assert isValidBST(my_tree)
    assert my_tree.is_avl()
    print(my_tree.height)
    print(my_tree)
    assert my_tree.height == 2, f"Expected height 2 after insertion, got {my_tree.height}"

    my_tree = AVLNode.delete(root=my_tree, key=10)
    assert isValidBST(my_tree)
    assert my_tree.is_avl()
    print(my_tree.height)
    print(my_tree)
    assert my_tree.height == 2, f"Expected height 2 after deletion, got {my_tree.height}"


def test_length():
    source = [9, 3, 20, None, None, 15, 25]
    length = len(list(filter(lambda x: x is not None, source)))
    my_tree: AVLNode = AVLNode.from_list(source)
    assert isValidBST(my_tree)
    assert my_tree.is_avl()
    assert my_tree.length == length, f"Expected length {length}, got {my_tree.length}"

    my_tree = AVLNode.insert(root=my_tree, key=10)
    length += 1
    assert (
        my_tree.length == length
    ), f"Expected length {length} after insertion, got {my_tree.length}"

    my_tree = AVLNode.delete(root=my_tree, key=20)
    length -= 1
    assert (
        my_tree.length == length
    ), f"Expected length {length} after deletion, got {my_tree.length}"

    my_tree = AVLNode.delete(root=my_tree, key=9)
    length -= 1
    assert (
        my_tree.length == length
    ), f"Expected length {length} after deletion, got {my_tree.length}"


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def test_in_order_dfs():
    POPULATION_SIZE = 1 * 10**2
    population = range(POPULATION_SIZE * 10)
    for _ in range(TEST_SIZE):
        sample = random.sample(population=population, k=POPULATION_SIZE)

        if not sample:
            return None
        queue = deque(sample)
        value = queue.popleft()
        root = AVLNode(value)
        control_root = AVLNode(value)
        assert id(root) != id(control_root)

        while queue:
            value = queue.popleft()
            if value is None:
                continue
            root = AVLNode.bst_insert(root=root, key=value)
            control_root = AVLNode.insert(root=control_root, key=value)

        assert isValidBST(root=root)
        assert isValidBST(root=control_root)
        assert control_root.is_avl()

        control_order = list(control_root.dfs_in_order_traverse())
        assert is_sorted(control_order)
        while not root.is_avl():
            root = AVLNode.avl_transform_and_validate(node=root)
            order = list(root.dfs_in_order_traverse())
            assert is_sorted(order)
            for a, b in zip(order, control_order):
                assert a == b
