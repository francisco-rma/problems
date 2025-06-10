from arrays_hashing.contains_duplicate import contains_duplicate


def test_contains_duplicate():
    """Test harness for group_anagrams."""
    print("Testing group_anagrams...")
    test_cases: list[list[int]] = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 1],
        [1],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 2],
    ]

    expected_results: list[bool] = [
        False,
        True,
        False,
        False,
        False,
        False,
        False,
    ]

    for i, test_case in enumerate(test_cases):
        result = contains_duplicate(test_case)
        assert result == expected_results[i], f"Test case {i + 1} failed: {test_case} -> {result}"
