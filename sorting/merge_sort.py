import timeit
from typing import Sequence
import numpy as np

ARRAY_SIZE: int = 10
TESTS_NUMBER: int = 100
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


def generate_n_tests():
    """Generation of lists for performance tests"""
    rng = np.random
    test_list = []
    i = 0

    while i < TESTS_NUMBER:
        test_list.append(rng.randint(low=0, high=1000, size=i))
        i += 1

    return test_list


def merge_sort(my_list: list) -> list[int]:
    """Merge sort"""
    if len(my_list) <= 1:
        return my_list

    midpoint = len(my_list) // 2
    left_array = my_list[:midpoint]
    right_array = my_list[midpoint:]

    left_array = merge_sort(left_array)

    right_array = merge_sort(right_array)

    merge(left=left_array, right=right_array, target=my_list)

    return my_list


def merge(left: list, right: list, target: list):
    """Merge"""
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            target[k] = left[i]
            i += 1
        else:
            target[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        target[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        target[k] = right[j]
        j += 1
        k += 1

    return target


def c_merge_sort(numbers: Sequence, n: int):
    """Cython merge sort"""
    return numbers


def merge_sort_time():
    """Perform merge sort"""
    setup_code = """
from __main__ import merge_sort, ARRAY_SIZE, index_ref, tests
"""

    test_code = """
mylist = tests[index_ref[0]]
merge_sort(mylist)"""

    test_list = generate_tests()

    for _ in test_list:
        i = 0
        times = []
        while i < REFINEMENT:
            times.append(timeit.timeit(setup=setup_code, stmt=test_code, number=REFINEMENT))
            i += 1

        time: float = np.format_float_positional(np.mean(times), precision=5)

        merge_sort_times.append(time)

        print(f"Test number {index_ref[0]}")
        print(
            f"Mean time for merge sort:\n {np.format_float_positional(np.mean(times), precision=5)} seconds"
        )
        index_ref[0] += 1


def validity_test() -> bool:
    """Checks whether or not the input sequence is sorted"""

    for index, numbers in enumerate(tests):
        print(f"Test number: {index}\n")
        start_size = len(numbers)
        unique, count = np.unique(numbers, return_counts=True)
        start_count = dict(zip(unique, count))

        merge_sort(numbers)
        end_size = len(numbers)
        unique, count = np.unique(numbers, return_counts=True)
        end_count = dict(zip(unique, count))
        is_sorted = np.all(numbers[:-1] <= numbers[1:])

        is_complete = (start_count == end_count) and (start_size == end_size)

        check = is_sorted and is_complete
        if not check:
            print("Array not sorted, aborting!")
            raise RuntimeError("Array not sorted")
        print("Array succesfully sorted, moving on")

    return True


def numpy_sort_time():
    """Numpy sorting function for performance comparison (defaults to quicksort)"""
    setup_code = """
from __main__ import merge_sort, ARRAY_SIZE, index_ref, tests
import numpy as np
"""

    test_code = """
np.sort(tests[index_ref[0]], kind='mergersort')"""

    test_list = generate_tests()

    for _ in test_list:
        i = 0
        times = []
        while i < REFINEMENT:
            times.append(timeit.timeit(setup=setup_code, stmt=test_code, number=REFINEMENT))
            i += 1

        time: float = np.format_float_positional(np.mean(times), precision=5)
        numpy_sort_times.append(time)

        print(f"Test number {index_ref[0]}")
        print(f"Mean time for numpy sort (quicksort):\n {time} seconds")
        index_ref[0] += 1


if __name__ == "__main__":
    # print(validity_test())
    # merge_sort_time()
    # index_ref[0] = 0

    # # c_merge_sort_time()
    # index_ref[0] = 0

    # numpy_sort_time()
    # index_ref[0] = 0
    # fig = plt.figure()

    # merge_sort_times = np.array(merge_sort_times).astype(float)
    # numpy_sort_times = np.array(numpy_sort_times).astype(float)
    # # c_merge_sort_times = np.array(c_merge_sort_times).astype(float)

    # data = zip(
    #     merge_sort_times,
    #     numpy_sort_times,
    #     # c_merge_sort_times,
    # )

    # MERGE_COLOR = "red"
    # NUMPY_COLOR = "green"
    # # CYTHON_COLOR = "blue"

    # ax1 = fig.add_subplot(1, 1, 1)

    # # scatter plot
    # ax1.set_xlim(right=TESTS_NUMBER, left=0)
    # ax1.set_ylim(top=np.max(merge_sort_times), bottom=0)
    # ax1.set_title("Mean test time")
    # ax1.set_xlabel("Test")
    # ax1.set_ylabel("Time (s)")

    # patch_merge = patches.Patch(color=MERGE_COLOR, label="merge sort")

    # patch_numpy = patches.Patch(color=NUMPY_COLOR, label="Numpy quicksort")

    # # patch_cython = patches.Patch(color=CYTHON_COLOR, label="Cython merge sort")

    # ax1.legend(
    #     handles=[
    #         patch_merge,
    #         patch_numpy,
    #         #  patch_cython
    #     ]
    # )

    # x = np.arange(0, TESTS_NUMBER, 1)

    # ax1.plot(x, merge_sort_times, color=MERGE_COLOR)
    # ax1.plot(x, numpy_sort_times, color=NUMPY_COLOR)
    # # ax1.plot(x, c_merge_sort_times, color=CYTHON_COLOR)

    # fig.show()
    # fig.savefig(f"merge_sort_n={ARRAY_SIZE}")
    # plt.show()

    # tests = generate_n_tests()
    tests = generate_tests()

    for test in tests:
        start_size = len(test)
        unique, count = np.unique(test, return_counts=True)
        start_count = dict(zip(unique, count))

        merge_sort(test)

        end_size = len(test)
        end_count = dict(zip(unique, count))
        bla = list(test)
        is_sorted = np.all(test[:-1] <= test[1:])

        is_complete = (start_count == end_count) and (start_size == end_size)
