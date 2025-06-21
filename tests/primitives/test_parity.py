from primitives.primitives import parity


def test_parity():
    """Test harness for parity function with different methods."""
    test_range = range(1, 10000)
    for test in test_range:
        reference_result = parity(x=test)
        bit_erasure_result = parity(x=test, method="bit_erasure")
        bit_grouping_result = parity(x=test, method="bit_grouping")
        assert reference_result == bit_erasure_result
        assert reference_result == bit_grouping_result
