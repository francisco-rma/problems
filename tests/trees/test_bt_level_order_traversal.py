from trees.bt_level_order_traversal import TreeNode


def test_bt_level_order_traversal():
    cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
        ([1, None, 2, None, 3], [[1], [2], [3]]),
        ([1, 2, None, 3, None, 4, None], [[1], [2], [3], [4]]),
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            [[5], [4, 8], [11, 13, 4], [7, 2, 5, 1]],
        ),
        ([10, 6, 15, 3, 8, None, 20], [[10], [6, 15], [3, 8, 20]]),
        ([1, 2, 3, None, 4, None, 5], [[1], [2, 3], [4, 5]]),
    ]
    for source, control in cases:
        root: TreeNode = TreeNode.from_list(source)
        if not root:
            assert control == []
            continue

        result = root.levelOrder(root)
        assert result == control, f"Failed for {root.__repr__}: expected {control}, got {result}"
