from operator import concat
import timeit
from turtle import color
from matplotlib import patches
import numpy as np
import matplotlib.pyplot as plt

size = 100
repeats = 10
refinement = 10

numpy_sort_times: list[float] = []
insertion_sort_times: list[float] = []
index_ref = [0]


def generate_tests():
    rng = np.random
    tests = []
    i = 0

    while i < 1000:
        tests.append(rng.randint(low=0, high=1000, size=size))
        i += 1

    return tests


tests = generate_tests()


def insertion_sort(list: list[int], n: int) -> list[int]:
    i = 1

    while i < n:
        key = list[i]
        j = i - 1

        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = key
        i += 1

    # in real life just use:
    # numbers = np.sort(numbers)

    return list


def insertion_sort_time():
    SETUP_CODE = '''
from __main__ import insertion_sort, size, index_ref, tests
'''

    TEST_CODE = '''
mylist = tests[index_ref[0]]
insertion_sort(mylist, size)'''

    global insertion_sort_times
    global repeats
    global refinement

    tests = generate_tests()

    for case in tests:
        times = timeit.repeat(setup=SETUP_CODE,
                              stmt=TEST_CODE,
                              repeat=repeats,
                              number=refinement)

        insertion_sort_times = concat(insertion_sort_times, times)

        print(f'Test number {index_ref[0]}')
        print(
            f'Mean time for insertion sort:\n {np.format_float_positional(np.mean(times), precision=5)} seconds')
        index_ref[0] += 1


def numpy_sort_time():
    SETUP_CODE = '''
from __main__ import insertion_sort, size, index_ref, tests
import numpy as np
'''

    TEST_CODE = '''
np.sort(tests[index_ref[0]])'''

    global numpy_sort_times
    global repeats
    global refinement

    tests = generate_tests()

    for case in tests:
        times = timeit.repeat(setup=SETUP_CODE,
                              stmt=TEST_CODE,
                              repeat=repeats,
                              number=refinement)

        numpy_sort_times = concat(numpy_sort_times, times)

        print(f'Test number {index_ref[0]}')
        print(
            f'Mean time for numpy sort (quicksort):\n {np.format_float_positional(np.mean(times), precision=5)} seconds')
        index_ref[0] += 1


def test(numbers: list[int]) -> bool:
    numbers = insertion_sort(list=numbers, n=1000)
    check = np.all(numbers[:-1] <= numbers[1:])
    print(check)
    return check


def validity_test(numbers: list[int]) -> bool:
    return np.all(numbers[:-1] <= numbers[1:])


def performance_test(numbers: list[int], index: list[int]):
    print(f'Test number: {index[0]}')
    index[0] += 1
    numbers = insertion_sort(list=numbers, n=len(numbers))
    return


if __name__ == "__main__":
    insertion_sort_time()
    index_ref[0] = 0
    numpy_sort_time()
    fig = plt.figure()

    data = zip(insertion_sort_times, numpy_sort_times)
    insertion_color = 'red'
    numpy_color = 'green'
    ax1 = fig.add_subplot(1, 1, 1)

    # scatter plot
    ax1.set_xlim(right=size, left=len(tests))
    ax1.set_ylim(top=np.max(insertion_sort_times), bottom=0)
    ax1.set_title('Mean test time')
    ax1.set_xlabel('Test')
    ax1.set_ylabel('Time (s)')

    patch_insertion = patches.Patch(
        color=insertion_color, label=f'Insertion sort')

    patch_numpy = patches.Patch(
        color=numpy_color, label=f'Numpy sort')

    ax1.legend(handles=[patch_insertion, patch_numpy])

    x = np.arange(0, repeats*len(tests), 1)

    ax1.plot(x, insertion_sort_times, color=insertion_color)
    ax1.plot(x, numpy_sort_times, color=numpy_color)

    fig.show()
    plt.show()
