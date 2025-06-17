from collections import deque
import numpy as np
from trees.avl_tree import AVLNode
from trees.valid_bst import isValidBST


def test_insertion():
    source = [9, 3, 20, None, None, 15, 25]
    rng = np.random.default_rng()
    my_tree: AVLNode = AVLNode.from_list(source)
    assert isValidBST(my_tree)

    if not my_tree:
        raise ValueError("Tree is empty, cannot perform insertion tests.")

    for index in range(100):
        insertion_target = rng.integers(low=0, high=1000, size=1)[0]
        result, parent = my_tree.insert(key=insertion_target)

        assert isValidBST(my_tree)
        assert parent is not None
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
    inserted_values: list[int] = []

    for _ in range(10000):
        val = rng.integers(low=1, high=1000, size=1)[0]
        my_tree.insert(key=val)
        inserted_values.append(val)
        assert isValidBST(my_tree)
        assert my_tree.contains(target=val)

    aux = my_tree.val
    my_tree.delete(key=aux)
    assert not my_tree.contains(target=aux)
    assert isValidBST(my_tree)

    queue = deque(set(inserted_values))
    while queue:
        val = queue.pop()
        my_tree.delete(key=val)
        for item in queue:
            assert my_tree.contains(
                target=item
            ), f"Item {item} should still be in the tree after deletion of {val}."
        assert not my_tree.contains(target=val)
        assert isValidBST(my_tree)
