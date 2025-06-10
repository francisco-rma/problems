import random
from arrays_hashing import parity_sort


def test_parity_sort():
    """Test harness for parity sort."""

    size = 10
    test_range = range(1, 100)

    for _ in test_range:
        tests = random.choices(test_range, k=size)
        print(f"\nInitial array: {tests}")
        result = parity_sort.parity_sort(values=tests)
        print(f"Result  array: {result}\n-------------------\n")
        assert parity_sort.validation(result)
