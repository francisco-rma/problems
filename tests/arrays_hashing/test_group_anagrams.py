from arrays_hashing.group_anagrams import group_anagrams


def test_group_anagrams():
    """Test harness for group_anagrams."""
    print("Testing group_anagrams...")
    test_cases: list[list[str]] = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "cba", "bca", "cab"],
        ["listen", "silent", "enlist"],
        ["rat", "tar", "art"],
        ["hello", "world"],
    ]

    expected_results: list[list[str]] = [
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        [[""]],
        [["a"]],
        [["abc", "cba", "bca", "cab"]],
        [["listen", "silent", "enlist"]],
        [["rat", "tar", "art"]],
        [["hello"], ["world"]],
    ]

    for i, test_case in enumerate(test_cases):
        result = list(map(set, group_anagrams(test_case)))
        control = list(map(set, expected_results[i]))
        assert len(result) == len(control), f"Test case {i + 1} failed: {test_case} -> {result}"

        for group in result:
            target = list(filter(lambda x: x == group, control))
            assert 0 < len(target) == 1
