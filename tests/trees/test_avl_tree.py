import numpy as np
from trees.avl_tree import AVLNode
from trees.valid_bst import isValidBST


def test_insertion():
    source = [9, 3, 20, None, None, 15, 25]

    rng = np.random.default_rng(42)  # Seed for reproducibility

    my_tree: AVLNode = AVLNode.from_list(source)

    assert isValidBST(my_tree)

    if not my_tree:
        raise ValueError("Tree is empty, cannot perform insertion tests.")

    for index in range(100):
        insertion_target = rng.integers(low=0, high=1000, size=1)[0]

        (result, parent) = my_tree.insert(key=insertion_target)
        print(my_tree)
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
