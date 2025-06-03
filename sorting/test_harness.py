# =======================================================
# Test harness
# =======================================================

import random
import quicksort

# =======================================================
# Quicksort
# =======================================================


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


num_tests = 10
size = 1000
value_range = range(-1000, 1000)

for _ in range(num_tests):
    arr = random.choices(value_range, k=size)
    arr_to_sort = arr.copy()
    quicksort.quicksort(arr_to_sort)
    assert is_sorted(arr_to_sort)

# =======================================================
# =======================================================
