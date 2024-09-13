import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    def calculate_time(rate: int) -> int:
        time = 0
        for value in piles:
            time += math.ceil(value / rate)
            if time > h:
                return 0

        return time

    left = 1
    right = max(piles)

    bph = right

    while left <= right:
        idx = left + ((right - left) // 2)

        time = calculate_time(idx)

        if time == 0:
            left = idx + 1
        else:
            bph = idx
            right = idx - 1

    return bph


piles = [30, 11, 23, 4, 20]
h = 6

result = minEatingSpeed(piles=piles, h=h)

print(result)
