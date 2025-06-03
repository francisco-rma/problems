# pylint: disable=global-statement,missing-module-docstring

import timeit
from matplotlib import patches
import numpy as np
import matplotlib.pyplot as plt

# import gman

ARRAY_SIZE: int = 1000
TESTS_NUMBER: int = 100
REFINEMENT: int = 10
# REPEATS: int = 1

insertion_sort_times: list[float] = []
c_insertion_sort_times: list[float] = []
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


def generate_n_tests():
    """Generation of lists for performance tests"""
    rng = np.random
    test_list = []
    i = 0

    while i < TESTS_NUMBER:
        test_list.append(rng.randint(low=0, high=1000, size=i))
        i += 1

    return test_list


tests = generate_n_tests()


def insertion_sort(numbers: list[int], n: int) -> list[int]:
    """Insertion Sort"""
    i = 1

    while i < n:
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key
        i += 1

    # in real life just use:
    # numbers = np.sort(numbers)

    return numbers


def insertion_sort_time():
    """Perform insertion sort"""
    setup_code = """
from __main__ import insertion_sort, ARRAY_SIZE, index_ref, tests
"""

    test_code = """
mylist = tests[index_ref[0]]
insertion_sort(mylist, len(mylist))"""

    test_list = generate_n_tests()

    for _ in test_list:
        i = 0
        times = []
        while i < REFINEMENT:
            times.append(
                timeit.timeit(setup=setup_code, stmt=test_code, number=REFINEMENT)
            )
            i += 1

        time: float = np.format_float_positional(np.mean(times), precision=5)

        global insertion_sort_times
        insertion_sort_times.append(time)

        print(f"Test number {index_ref[0]}")
        print(
            f"Mean time for insertion sort:\n {np.format_float_positional(np.mean(times), precision=5)} seconds"
        )
        index_ref[0] += 1


def numpy_sort_time():
    """Numpy sorting function for performance comparison (defaults to quicksort)"""
    setup_code = """
from __main__ import insertion_sort, ARRAY_SIZE, index_ref, tests
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


def c_insertion_sort(numbers: list[int], n: int) -> list[int]:
    """Insertion Sort"""

    # return gman.insertion_sort(numbers, n)


def c_insertion_sort_time():
    """Perform insertion sort"""
    setup_code = """
from __main__ import c_insertion_sort, ARRAY_SIZE, index_ref, tests
"""

    test_code = """
mylist = tests[index_ref[0]]
c_insertion_sort(mylist, len(mylist))"""

    test_list = generate_n_tests()

    for _ in test_list:
        i = 0
        times = []
        while i < REFINEMENT:
            times.append(
                timeit.timeit(setup=setup_code, stmt=test_code, number=REFINEMENT)
            )
            i += 1

        time: float = np.format_float_positional(np.mean(times), precision=5)

        c_insertion_sort_times.append(time)

        print(f"Test number {index_ref[0]}")
        print(
            f"Mean time for cython insertion sort:\n {np.format_float_positional(np.mean(times), precision=5)} seconds"
        )
        index_ref[0] += 1


def validity_test(numbers: list[int]) -> bool:
    """Checks whether or not the input sequence is sorted"""

    return np.all(numbers[:-1] <= numbers[1:])


def performance_test(numbers: list[int], index: list[int]):
    """Generates a graphical view of time ellapsed to run the algorithm"""
    print(f"Test number: {index[0]}")
    index[0] += 1
    numbers = insertion_sort(numbers=numbers, n=len(numbers))
    return


if __name__ == "__main__":
    insertion_sort_time()
    index_ref[0] = 0

    c_insertion_sort_time()
    index_ref[0] = 0

    numpy_sort_time()
    index_ref[0] = 0
    fig = plt.figure()

    insertion_sort_times = np.array(insertion_sort_times).astype(float)
    numpy_sort_times = np.array(numpy_sort_times).astype(float)
    c_insertion_sort_times = np.array(c_insertion_sort_times).astype(float)

    data = zip(
        insertion_sort_times,
        numpy_sort_times,
        c_insertion_sort_times,
    )

    INSERTION_COLOR = "red"
    NUMPY_COLOR = "green"
    CYTHON_COLOR = "blue"

    ax1 = fig.add_subplot(1, 1, 1)

    # scatter plot
    ax1.set_xlim(right=TESTS_NUMBER, left=0)
    ax1.set_ylim(top=np.max(insertion_sort_times), bottom=0)
    ax1.set_title("Mean test time")
    ax1.set_xlabel("Test")
    ax1.set_ylabel("Time (s)")

    patch_insertion = patches.Patch(color=INSERTION_COLOR, label="Insertion sort")

    patch_numpy = patches.Patch(color=NUMPY_COLOR, label="Numpy quicksort")

    patch_cython = patches.Patch(color=CYTHON_COLOR, label="Cython insertion sort")

    ax1.legend(handles=[patch_insertion, patch_numpy, patch_cython])

    x = np.arange(0, TESTS_NUMBER, 1)

    ax1.plot(x, insertion_sort_times, color=INSERTION_COLOR)
    ax1.plot(x, numpy_sort_times, color=NUMPY_COLOR)
    ax1.plot(x, c_insertion_sort_times, color=CYTHON_COLOR)

    fig.show()
    fig.savefig(f"sorting/insertion-sort/insertion_sort_n={ARRAY_SIZE}")
    plt.show()
