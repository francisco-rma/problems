import collections
import timeit
from matplotlib import patches
import numpy as np
import matplotlib.pyplot as plt

ARRAY_SIZE: int = 1000
TESTS_NUMBER: int = 10
REFINEMENT: int = 10

merge_sort_times: list[float] = []
c_merge_sort_times: list[float] = []
numpy_sort_times: list[float] = []
index_ref = [0]


def generate_tests():
    """Generation of lists for performance tests"""
    rng = np.random
    test_list = []
    i = 0

    while i < TESTS_NUMBER:
        test_list.append(rng.randint(low=0, high=1000, size=ARRAY_SIZE))
        i += 1

    return test_list


tests = generate_tests()


def merge_sort(numbers: collections, n: int):
    return numbers


def c_merge_sort(numbers: collections, n: int):
    return numbers


def merge_sort_time():
    """Perform merge sort"""
    setup_code = """
from __main__ import merge_sort, ARRAY_SIZE, index_ref, tests
"""

    test_code = """
mylist = tests[index_ref[0]]
merge_sort(mylist, ARRAY_SIZE)"""

    test_list = generate_tests()

    for _ in test_list:
        i = 0
        times = []
        while i < REFINEMENT:
            times.append(
                timeit.timeit(setup=setup_code, stmt=test_code, number=REFINEMENT)
            )
            i += 1

        time: float = np.format_float_positional(np.mean(times), precision=5)

        global merge_sort_times
        merge_sort_times.append(time)

        print(f"Test number {index_ref[0]}")
        print(
            f"Mean time for merge sort:\n {np.format_float_positional(np.mean(times), precision=5)} seconds"
        )
        index_ref[0] += 1


def numpy_sort_time():
    """Numpy sorting function for performance comparison (defaults to quicksort)"""
    setup_code = """
from __main__ import merge_sort, ARRAY_SIZE, index_ref, tests
import numpy as np
"""

    test_code = """
np.sort(tests[index_ref[0]])"""

    test_list = generate_tests()

    for _ in test_list:
        i = 0
        times = []
        while i < REFINEMENT:
            times.append(
                timeit.timeit(setup=setup_code, stmt=test_code, number=REFINEMENT)
            )
            i += 1

        time: float = np.format_float_positional(np.mean(times), precision=5)
        numpy_sort_times.append(time)

        print(f"Test number {index_ref[0]}")
        print(f"Mean time for numpy sort (quicksort):\n {time} seconds")
        index_ref[0] += 1


if __name__ == "__main__":
    merge_sort_time()
    index_ref[0] = 0

    # c_merge_sort_time()
    index_ref[0] = 0

    numpy_sort_time()
    index_ref[0] = 0
    fig = plt.figure()

    merge_sort_times = np.array(merge_sort_times).astype(float)
    numpy_sort_times = np.array(numpy_sort_times).astype(float)
    c_merge_sort_times = np.array(c_merge_sort_times).astype(float)

    data = zip(
        merge_sort_times,
        numpy_sort_times,
        # c_merge_sort_times,
    )

    MERGE_COLOR = "red"
    NUMPY_COLOR = "green"
    CYTHON_COLOR = "blue"

    ax1 = fig.add_subplot(1, 1, 1)

    # scatter plot
    ax1.set_xlim(right=TESTS_NUMBER, left=0)
    ax1.set_ylim(top=np.max(merge_sort_times), bottom=0)
    ax1.set_title("Mean test time")
    ax1.set_xlabel("Test")
    ax1.set_ylabel("Time (s)")

    patch_merge = patches.Patch(color=MERGE_COLOR, label="merge sort")

    patch_numpy = patches.Patch(color=NUMPY_COLOR, label="Numpy quicksort")

    # patch_cython = patches.Patch(color=CYTHON_COLOR, label="Cython merge sort")

    ax1.legend(
        handles=[
            patch_merge,
            patch_numpy,
            #  patch_cython
        ]
    )

    x = np.arange(0, TESTS_NUMBER, 1)

    ax1.plot(x, merge_sort_times, color=MERGE_COLOR)
    ax1.plot(x, numpy_sort_times, color=NUMPY_COLOR)
    # ax1.plot(x, c_merge_sort_times, color=CYTHON_COLOR)

    fig.show()
    fig.savefig(f"merge_sort_n={ARRAY_SIZE}")
    plt.show()
