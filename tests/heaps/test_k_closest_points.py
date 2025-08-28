import math
import random
import time
import numpy as np
from heaps.k_closest_points import k_closest

POP_SIZE = 10**6
SAMPLE_COUNT = 10**5
TOLERANCE = 10**-6


def test_k_closest_points():
    source = list(
        zip(
            random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT),
            random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT),
        )
    )
    test = k_closest(source, 5)
    print(test)

    source.sort(key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))

    for idx, (x_test, y_test) in enumerate(test):
        assert x_test == source[idx][0]
        assert y_test == source[idx][1]


def test_k_closest_distances():
    source = list(
        zip(
            random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT),
            random.sample(population=range(POP_SIZE), k=SAMPLE_COUNT),
        )
    )
    test = list(map(lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2), k_closest(source, 5)))
    control = sorted(list(map(lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2), source)))
    for idx, test_value in enumerate(test):
        assert abs(test_value - control[idx]) <= TOLERANCE
