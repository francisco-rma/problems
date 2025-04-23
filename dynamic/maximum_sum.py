from functools import lru_cache
import random
import numpy as np


def maximum_gain(coins: list[int]):
    @lru_cache(None)
    def compute_maximum_coins(a: int, b: int) -> int:
        if a > b:
            return 0

        iteration = (b - a) % 2
        if iteration == 0:
            pick_left = coins[a] + compute_maximum_coins(a + 1, b)
            pick_right = coins[b] + compute_maximum_coins(a, b - 1)
        else:
            pick_left = compute_maximum_coins(a + 1, b)
            pick_right = compute_maximum_coins(a, b - 1)

        return max(pick_left, pick_right)

    return compute_maximum_coins(0, len(coins) - 1)


def maximum_gainV2(coins: list[int]):
    @lru_cache(None)
    def compute_maximum_coins_v2(a: int, b: int) -> int:
        if a > b:
            return 0

        pick_left = coins[a] + min(
            compute_maximum_coins_v2(a + 2, b), compute_maximum_coins_v2(a + 1, b - 1)
        )
        pick_right = coins[b] + min(
            compute_maximum_coins_v2(a + 1, b - 1), compute_maximum_coins_v2(a, b - 2)
        )

        return max(pick_left, pick_right)

    return compute_maximum_coins_v2(0, len(coins) - 1)


values = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10]


def check_max_iterations():
    with open("iteration", "w+") as f:
        for i in range(490, 10000):
            f.truncate(0)
            f.write(f"{i}")
            values = random.choices(range(100000), k=i)
            # result = maximum_gain(values)
            resultV2 = maximum_gainV2(values)
            # assert resultV2 <= result
            print(f"\n-------i={i}-------")
            # print(f"result - all paths: {result}")
            print(f"resultV2 - with strategy: {resultV2}")
            print(f"-------i={i}-------\n")


iter_n = None
check_max_iterations()
with open("iteration", "r") as f:
    # print(str(f.read()).split("\x00"))
    iter_n = int(str(f.read()).split("\x00")[-1])

print(iter_n)
values = random.choices(range(100000), k=iter_n)
# result = maximum_gain(values)
resultV2 = maximum_gainV2(values)
# assert resultV2 <= result
print(f"\n-------i={iter_n}-------")
# print(f"result - all paths: {result}")
print(f"resultV2 - with strategy: {resultV2}")
print(f"-------i={iter_n}-------\n")
