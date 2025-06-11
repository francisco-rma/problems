import random
from sorting.quicksort import quicksort


def test_quicksort():
    """Test harness for bubble sort."""
    SIZE = 1000
    for _ in range(10):
        test = [random.randint(0, 100) for _ in range(SIZE)]
        result = test.copy()

        test.sort()
        quicksort(result)

        assert all(a == b for a, b in zip(result, test))
        assert all(result[i] <= result[i + 1] for i in range(SIZE - 1))


def test_quicksort_unique():
    """Test harness for bubble sort."""
    SIZE = 100
    POPULATION = range(SIZE * 10)
    for _ in range(10):
        test = random.sample(population=POPULATION, k=SIZE)
        result = test.copy()

        test.sort()
        quicksort(result)

        assert all(a == b for a, b in zip(result, test))
        assert all(result[i] <= result[i + 1] for i in range(SIZE - 1))
