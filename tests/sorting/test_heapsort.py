import random

from sorting.heapsort import heapsort


def test_heapsort():
    """Test harness for heap sort."""
    SIZE = 1000
    for _ in range(10):
        test = [random.randint(0, 100) for _ in range(SIZE)]
        heapsort(test)
        control = sorted(test)

        assert all(a == b for a, b in zip(control, test))
        assert all(test[i] <= test[i + 1] for i in range(SIZE - 1))


def test_heapsort_unique():
    """Randomized test harness for heap sort."""
    SIZE = 100
    POPULATION = range(SIZE * 10)
    for _ in range(10):
        test = random.sample(population=POPULATION, k=SIZE)
        heapsort(test)
        control = sorted(test)

        assert all(a == b for a, b in zip(control, test))
        assert all(test[i] <= test[i + 1] for i in range(SIZE - 1))


def test_heapsort_fuzz():
    for i in range(2, 6):
        SIZE = 10**i
        POPULATION = range(SIZE * 10)
        for _ in range(10):
            test = random.sample(population=POPULATION, k=SIZE)
            heapsort(test)
            control = sorted(test)

            assert all(a == b for a, b in zip(control, test))
            assert all(test[i] <= test[i + 1] for i in range(SIZE - 1))
