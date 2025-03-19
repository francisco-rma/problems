from collections.abc import Sequence


def hello_world(name):
    print('Hello World')


def insertion_sort(numbers, n: int):
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