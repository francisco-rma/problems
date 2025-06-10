# =======================================================
# Parity
# =======================================================

import random

from primitives.primitives import is_power_of_two, parity


test_range = range(1, 10000)
size = 1000

tests = random.choices(test_range, k=size)

for test in test_range:
    print(f"\nTest value: {test:008b}")
    reference_result = parity(x=test)
    bit_erasure_result = parity(x=test, method="bit_erasure")
    bit_grouping_result = parity(x=test, method="bit_grouping")

    print(f"reference_result: {reference_result}")
    print(f"bit_erasure_result: {bit_erasure_result}")
    print(f"bit_grouping_result: {bit_grouping_result}")
    print("\n------------------")

    assert reference_result == bit_erasure_result
    assert reference_result == bit_grouping_result

# =======================================================
# =======================================================


# =======================================================
# Is a power of two
# =======================================================

true_values = [2**n for n in range(2, 1000)]
false_values = [2**n - 1 for n in range(2, 1000)]

for success_candidate, fail_candidate in zip(true_values, false_values):
    assert is_power_of_two(success_candidate)
    assert not is_power_of_two(fail_candidate)

# =======================================================
# =======================================================
