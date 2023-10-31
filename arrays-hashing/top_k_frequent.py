from typing import List

import numpy as np


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}
    frequency = [[] for i in range(len((nums)) + 1)]

    for _, element in enumerate(nums):
        counter[element] = 1 + counter.get(element, 0)

    for number, count in counter.items():
        frequency[count].append([number, count])

    return_list = []

    j = 0
    i = len(frequency) - 1

    while i > 0 and len(return_list) < k:
        candidates = frequency[i]
        if len(candidates) > 0:
            return_list.append(candidates[j])
            j += 1
        i -= 1
    return return_list


if __name__ == "__main__":
    rng = np.random
    input_list = rng.randint(low=0, high=1000, size=1000)
    answer = topKFrequent(input_list, 5)
    print(answer)
