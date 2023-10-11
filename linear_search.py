"""Module providing tools to measure execution time"""
import timeit
from matplotlib import patches, pyplot as plt
import numpy as np

ARRAY_SIZE: int = 1000
TEST_NUM: int = 50
REPEATS: int = 1
REFINEMENT: int = 1
index_ref = [0]
linear_search_times: list[float] = []
null_checker: list[int | None] = []


def linear_search(array: list[int], target: int) -> int | None:
    """Linear search"""
    print(f"Looking for {target}")
    idx = 1
    comparison = array[0]

    while comparison != target and idx < len(array):
        comparison = array[idx]
        idx += 1

    if idx >= len(array):
        print("Value not found!")
        null_checker.append(None)
        return None

    print(f"Found value {target} at index {idx - 1}:  {target} = {array[idx-1]}")
    null_checker.append(0)
    return idx - 1


def generate_tests():
    """Teste generation"""
    rng = np.random
    test_list = []
    i = 0

    while i < TEST_NUM:
        print("Generating tests...")
        test_list.append(
            [rng.randint(low=0, high=1000, size=ARRAY_SIZE), rng.randint(0, 1000)]
        )
        i += 1

    return test_list


tests = generate_tests()


def linear_search_time():
    """Linear search timing test"""
    setup_code = """
from __main__ import linear_search, ARRAY_SIZE, index_ref, tests
import numpy as np
"""

    test_code = """
linear_search(tests[index_ref[0]][0],tests[index_ref[0]][1])"""
    i = 0
    while i < len(tests):
        times = timeit.repeat(
            setup=setup_code, stmt=test_code, repeat=REPEATS, number=REFINEMENT
        )

        # linear_search_times = concat(linear_search_times, times)
        linear_search_times.append(np.amin(times))

        print(f"Test number {index_ref[0]}")
        print(
            f"Mean time for linear search:\n {np.format_float_positional(np.mean(times), precision=5)} seconds"
        )
        index_ref[0] += 1
        i += 1


if __name__ == "__main__":
    index_ref[0] = 0
    linear_search_time()

    def map_null_instances(value: int | None) -> float:
        """Mapping test indices that did not contain the searched value"""

        if value is None:
            return np.amax(linear_search_times)
        return 0.0

    np_null_checker = list(map(map_null_instances, null_checker))

    fig = plt.figure()

    data = linear_search_times
    LINEAR_SEARCH_COLOR = "green"
    NULL_CHECKER_COLOR = "red"
    ax1 = fig.add_subplot(1, 1, 1)

    # linear plot
    ax1.set_xlim(right=TEST_NUM, left=0)
    ax1.set_ylim(top=np.amax(linear_search_times), bottom=0)
    ax1.set_title("Mean test time")
    ax1.set_xlabel("Test")
    ax1.set_ylabel("Time (s)")

    patch_linear_search = patches.Patch(
        color=LINEAR_SEARCH_COLOR,
        label=f"Linear search, mean: {np.format_float_positional(np.mean(linear_search_times), precision=5)} seconds",
    )

    ax1.legend(handles=[patch_linear_search])

    x = np.arange(0, TEST_NUM, 1)

    # ax1.plot(x, insertion_sort_times, color=insertion_color)
    # ax1.plot(x, linear_search_times, color=LINEAR_SEARCH_COLOR)
    ax1.scatter(x, linear_search_times, color=LINEAR_SEARCH_COLOR)
    ax1.scatter(x, np_null_checker, color=NULL_CHECKER_COLOR, s=2)

    fig.show()
    plt.show()
