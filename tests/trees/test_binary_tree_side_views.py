from trees.binary_tree_side_views import TreeNode


def test_unit():
    tests = [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
        ([1, None, 3], [1, 3]),
        ([], []),
        ([None], [None]),
        ([1, 2, 3], [1, 3]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 7]),
    ]

    for sample, result in tests:
        root = TreeNode.lst_from_list(sample)
        assert TreeNode.right_side_view(root) == result
