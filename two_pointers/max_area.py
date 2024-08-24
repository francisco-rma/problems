import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def max_area_slow(heights: list[int]) -> tuple[int, int]:
    """Calculate the maximum area of an array of integers representing heights with an O(n^2) algorithm"""

    def volume(start, end):
        return abs(start - end) * min(heights[start], heights[end])

    if len(heights) == 0:
        return 0, 0

    container = volume(0, len(heights) - 1)
    start = datetime.now()
    for i in range(len(heights)):
        for j in range(len(heights)):
            container = max(container, volume(i, j))

    return container, (datetime.now() - start).total_seconds()


def max_area(heights: list[int]) -> tuple[int, int]:
    """Calculate the maximum area of an array of integers representing heights"""

    def volume(start, end):
        return abs(start - end) * min(heights[start], heights[end])

    if len(heights) == 0:
        return 0, 0

    min_idx = 0
    max_idx = len(heights) - 1
    container = volume(min_idx, max_idx)
    start = datetime.now()
    while min_idx < max_idx:
        if heights[min_idx] < heights[max_idx]:
            min_idx += 1
        else:
            max_idx -= 1

        container = max(container, volume(min_idx, max_idx))

    return container, (datetime.now() - start).total_seconds()


rng = np.random.default_rng()

times = []
slow_times = []
sizes = []

for i in range(0, 1000):
    heights = rng.integers(1, 100, size=i)
    result, time = max_area(heights)
    times.append(time)

    result, slow_time = max_area_slow(heights)
    slow_times.append(slow_time)

    sizes.append(i)

colors = ["blue", "red"]
plt.bar(
    sizes,
    times,
)
plt.bar(sizes, slow_times, color=["red"])
plt.bar(sizes, times, color=["blue"])
plt.show()
