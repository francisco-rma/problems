import time
import numpy as np
import matplotlib.pyplot as plt
import sorting.merge_sort
import sorting.merge_sort.merge_sort
from utils import decorators
import sorting


def binary_count(values: list[int], target: int) -> int:
    if not values or values[-1] < target:
        None

    left = 0

    right = len(values) - 1

    while left <= right:
        midpoint = left + ((right - left) // 2)

        if values[midpoint] <= target and values[midpoint + 1] > target:
            return midpoint

        elif values[midpoint] < target:
            left = midpoint + 1

        else:
            right = midpoint - 1

    return 0


# @decorators.print_runtime
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    A, B = nums1, nums2

    if len(A) > len(B):
        A, B = B, A

    half = (len(A) + len(B)) // 2

    left, right = 0, len(A) - 1

    while True:
        i = left + ((right - left) // 2)
        j = half - i - 2

        leftA = A[i] if i >= 0 else float("-infinity")
        leftB = B[j] if j >= 0 else float("-infinity")
        rightA = A[i + 1] if (i + 1) < len(A) else float("infinity")
        rightB = B[j + 1] if (j + 1) < len(B) else float("infinity")

        if leftA > rightB:
            right = i - 1

        elif leftB > rightA:
            left = i + 1

        else:
            if (len(A) + len(B)) % 2 == 0:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            else:
                return min(rightA, rightB)


rng = np.random.default_rng()

results = []
sizes = np.linspace(1, 500000, 10000, dtype=int)
for i in sizes:

    j = 0
    raw_results = []
    while j < 10:
        divisor = rng.integers(0, i + 1)

        nums1 = np.sort(rng.integers(0, 1000, size=(i - divisor + 1)))

        # nums1_test2 = sorting.merge_sort.merge_sort.merge_sort(nums1)
        # assert np.array_equal(nums1_test1, nums1_test2)

        nums2 = np.sort(rng.integers(0, 1000, size=divisor))
        # print(len(nums1), len(nums2))

        start = time.perf_counter()
        median = findMedianSortedArrays(nums1=nums1, nums2=nums2)
        runtime = time.perf_counter() - start
        # print(f"Result: {median}")
        raw_results.append(runtime)
        j += 1

    avg_time = np.mean(raw_results)
    # print(f"Iteration:{i}  --->  avg time: {avg_time}\n")
    results.append(avg_time)


plt.plot(sizes, results)
plt.show()
