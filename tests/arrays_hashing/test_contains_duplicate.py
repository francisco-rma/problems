from arrays_hashing.contains_duplicate import contains_duplicate


def test_contains_duplicate():
    """Test harness for contains_duplicate."""
    print("Testing contains_duplicate...")
    cases: list[tuple[list[int], bool]] = [
        ([1, 2, 3, 4, 5], False),
        ([1, 2, 3, 4, 5, 1], True),
        ([1], False),
        ([1, 2, 3, 4, 5, 6], False),
        ([1, 2, 3, 4, 5, 6, 7], False),
        ([1, 2, 3, 4, 5, 6, 7, 8], False),
        ([1, 2], False),
        ([1, 1], True),
        ([1, 2, 3, 2], True),
        ([1, 2, 4, 5, 6, 7, 8, 9, 0, 0], True),
    ]

    for i, (test_case, control) in enumerate(cases):
        result = contains_duplicate(test_case)
        assert result == control, f"Test case {i + 1} failed: {test_case} -> {result}"


def test_fuzzy():
    """Fuzzy test for contains_duplicate."""
    import random

    SIZE = 1000
    population = range(SIZE)
    for _ in range(100):
        test_case = random.sample(population, random.randint(1, SIZE))
        has_duplicate = random.choice([True, False])
        if has_duplicate:
            # Introduce a duplicate
            test_case.append(random.choice(test_case))

        control = has_duplicate
        result = contains_duplicate(test_case)
        assert result == control, f"Fuzzy test failed: {test_case} -> {result}"
