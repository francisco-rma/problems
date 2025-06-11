from trees.valid_bst import TreeNode


def test_valid_bst():
    cases = [
        ([3, 9, 20, None, None, 15, 7], False),
        ([1], True),
        ([], True),
        ([1, 2, 3, 4, 5, 6, 7], False),
        ([1, None, 2, None, 3], True),
        ([1, 2, None, 3, None, 4, None], False),
        ([10, 6, 15, 3, 8, None, 20], True),
        ([1, 2, 3, None, 4, None, 5], False),
        ([2, 2, 2], False),
        ([5, 4, 6, None, None, 3, 7], False),
    ]
    for source, control in cases:
        root: TreeNode = TreeNode.from_list(source)

        result = TreeNode.isValidBST(root)
        assert result == control, f"Failed for {root}: expected {control}, got {result}"


def test_simple_cases():
    # Valid BST
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert TreeNode.isValidBST(root) is True

    # Invalid BST (left child > root)
    root = TreeNode(2, TreeNode(5), TreeNode(3))
    assert TreeNode.isValidBST(root) is False

    # Invalid BST (right child < root)
    root = TreeNode(2, TreeNode(1), TreeNode(0))
    assert TreeNode.isValidBST(root) is False

    # Single node
    root = TreeNode(1)
    assert TreeNode.isValidBST(root) is True

    # Empty tree
    assert TreeNode.isValidBST(None) is True
