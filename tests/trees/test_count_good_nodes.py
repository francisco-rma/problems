from trees.count_good_nodes import TreeNode, goodNodes


def test_valid_bst():
    cases = [
        ([1], 1),
        ([2, 1, 1, 3, None, 1, 5], 3),
        ([3, 3, None, 4, 2], 3),
    ]
    for source, control in cases:
        root: TreeNode = TreeNode.from_list(source)

        result = goodNodes(root)
        assert result == control, f"Failed for {root}: expected {control}, got {result}"
