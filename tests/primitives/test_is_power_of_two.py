from primitives.primitives import is_power_of_two


def test_is_power_of_two():
    """Test harness for is_power_of_two function."""
    true_values = [2**n for n in range(2, 1000)]
    false_values = [2**n - 1 for n in range(2, 1000)]
    for success_candidate, fail_candidate in zip(true_values, false_values):
        assert is_power_of_two(success_candidate)
        assert not is_power_of_two(fail_candidate)
