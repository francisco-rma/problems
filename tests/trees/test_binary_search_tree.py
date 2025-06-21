from collections import deque
import numpy as np
from trees.binary_search_tree import BSTNode
from trees.valid_bst import isValidBST


TEST_SIZE = 1 * 10**3


def test_bst_insert_and_contains():
    root = BSTNode(10)
    values = [5, 15, 3, 7, 12, 18]
    for v in values:
        root = BSTNode.insert(root, v)
    for v in [10] + values:
        assert root.contains(v)
    assert not root.contains(100)
    assert not root.contains(-1)


def test_bst_insert_duplicates():
    root = BSTNode(10)
    root = BSTNode.insert(root, 10)
    root = BSTNode.insert(root, 10)
    # Should not create duplicate nodes
    count = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == 10:
            count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    assert count == 1


def test_bst_delete_leaf():
    root = BSTNode(10)
    root = BSTNode.insert(root, 5)
    root = BSTNode.insert(root, 15)
    root = BSTNode.delete(root, 5)
    assert not root.contains(5)
    assert root.contains(10)
    assert root.contains(15)


def test_bst_delete_one_child():
    root = BSTNode(10)
    root = BSTNode.insert(root, 5)
    root = BSTNode.insert(root, 2)
    root = BSTNode.delete(root, 5)
    assert not root.contains(5)
    assert root.contains(2)
    assert root.contains(10)


def test_bst_delete_two_children():
    root = BSTNode(10)
    for v in [5, 15, 2, 7, 12, 18]:
        root = BSTNode.insert(root, v)
    root = BSTNode.delete(root, 5)
    assert not root.contains(5)
    for v in [2, 7, 10, 12, 15, 18]:
        assert root.contains(v)


def test_bst_delete_root():
    root = BSTNode(10)
    for v in [5, 15]:
        root = BSTNode.insert(root, v)
    root = BSTNode.delete(root, 10)
    assert not root.contains(10)
    assert root.contains(5)
    assert root.contains(15)


def test_bst_min_max():
    root = BSTNode(10)
    for v in [5, 15, 2, 7, 12, 18]:
        root = BSTNode.insert(root, v)
    min_node, _ = root.min()
    max_node, _ = root.max()
    assert min_node.val == 2
    assert max_node.val == 18


def test_bst_repr_and_display():
    root = BSTNode(10)
    for v in [5, 15, 2, 7]:
        root = BSTNode.insert(root, v)
    s = repr(root)
    assert isinstance(s, str)
    assert "10" in s
    assert "5" in s
    assert "15" in s


def test_bst_in_order_traversal():
    # Helper for in-order traversal
    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node.val] + in_order(node.right)

    vals = [10, 5, 15, 2, 7, 12, 18]
    root = BSTNode(vals[0])
    for v in vals[1:]:
        root = BSTNode.insert(root, v)
    result = in_order(root)
    assert result == sorted(vals)


def test_bst_from_list():
    assert BSTNode.from_list([]) is None
    root: BSTNode = BSTNode.from_list([10, 5, 15, 2, 7, 12, 18])
    for v in [10, 5, 15, 2, 7, 12, 18]:
        assert root.contains(v)


def test_from_list():
    rng = np.random.default_rng()
    source = rng.integers(low=0, high=1000, size=TEST_SIZE)
    my_tree: BSTNode = BSTNode.from_list(source)
    assert isValidBST(my_tree)


def test_insertion():
    source = [9, 3, 20, None, None, 15, 25]
    rng = np.random.default_rng()
    my_tree: BSTNode = BSTNode.from_list(source)
    assert isValidBST(my_tree)

    if not my_tree:
        raise ValueError("Tree is empty, cannot perform insertion tests.")

    for _ in range(TEST_SIZE):
        insertion_target = rng.integers(low=0, high=1000, size=1)[0]
        my_tree = BSTNode.insert(root=my_tree, key=insertion_target)
        assert my_tree
        assert isValidBST(my_tree)
        assert my_tree.contains(
            target=insertion_target
        ), f"Target {insertion_target} not found in the tree after insertion."

        node, _ = my_tree.binary_search(target=insertion_target)
        assert node is not None and node.val == insertion_target


def test_deletion():
    source = [0]
    rng = np.random.default_rng()
    my_tree: BSTNode = BSTNode.from_list(source)

    inserted_values: list[int] = []

    for _ in range(TEST_SIZE):
        val = rng.integers(low=1, high=1000, size=1)[0]
        if my_tree.contains(val):
            continue

        my_tree = BSTNode.insert(root=my_tree, key=val)

        inserted_values.append(val)
        assert isValidBST(my_tree)
        assert my_tree.contains(target=val)

    aux = my_tree.val
    my_tree = BSTNode.delete(root=my_tree, key=aux)
    assert not my_tree.contains(target=aux)
    assert isValidBST(my_tree)

    my_tree = BSTNode.insert(root=my_tree, key=aux)
    assert my_tree.contains(target=aux)
    assert isValidBST(my_tree)

    queue = deque(set(inserted_values))
    while queue:
        val = queue.pop()
        node, parent = my_tree.binary_search(target=val)
        assert node is not None and node.val == val

        my_tree = BSTNode.delete(root=my_tree, key=val)

        assert isValidBST(my_tree)

        for item in queue:
            assert my_tree.contains(
                target=item
            ), f"Item {item} should still be in the tree after deletion of {val}."
        assert not my_tree.contains(target=val)
