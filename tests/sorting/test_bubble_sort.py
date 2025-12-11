import random

from sorting.bubble_sort import bubble_sort


def test_bubble_sort():
    """Test harness for bubble sort."""
    SIZE = 1000
    for _ in range(10):
        test = [random.randint(0, 100) for _ in range(SIZE)]
        result = bubble_sort(test)
        test.sort()

        assert all(a == b for a, b in zip(result, test))
        assert all(result[i] <= result[i + 1] for i in range(SIZE - 1))


def test_bubble_sort_unique():
    """Test harness for bubble sort."""
    SIZE = 100
    POPULATION = range(SIZE * 10)
    for _ in range(10):
        test = random.sample(population=POPULATION, k=SIZE)
        result = bubble_sort(test)
        test.sort()

        assert all(a == b for a, b in zip(result, test))
        assert all(result[i] <= result[i + 1] for i in range(SIZE - 1))


def test_bubble_sort_fuzz():
    for i in range(2, 5):
        SIZE = 10**i
        POPULATION = range(SIZE * 10)
        for _ in range(10):
            test = random.sample(population=POPULATION, k=SIZE)
            control = sorted(test)
            test = bubble_sort(test)

            assert all(a == b for a, b in zip(control, test))
            assert all(test[i] <= test[i + 1] for i in range(SIZE - 1))
