import random


def get_leftmost_bit(x: int) -> int:
    count = 0
    while x > 0:
        x >>= 1
        count += 1

    return count


def count_1_bits(x) -> int:
    count = 0
    while x:
        count += x & 1
        x >>= 1

    return count


def parity(x, method: str = "bruteforce") -> int:
    match method:
        case "bruteforce":
            result = 0
            while x:
                result ^= x & 1
                x >>= 1
            return result

        case "bit_erasure":
            result = 0
            while x:
                result ^= 1
                x &= x - 1
            return result

        case "bit_grouping":
            # bit_count = get_leftmost_bit(x)

            # even_remainder = bit_count & 1
            # bit_count = bit_count - even_remainder if even_remainder else bit_count >> 1

            # print(f"\n{bit_count:008b}")
            # print(f"{x:008b}\n-----------------")
            # while bit_count:
            #     x ^= x >> bit_count
            #     bit_count >>= 1
            #     print(f"\n{bit_count:008b}")
            #     print(f"{x:008b}\n-----------------")

            x ^= x >> 32
            x ^= x >> 16
            x ^= x >> 8
            x ^= x >> 4
            x ^= x >> 2
            x ^= x >> 1

            return x & 1

        case _:
            return 0


def right_propagate(x: int):
    """
    Propagates the rightmost set bit to the right.\n
    """
    idx = x & -x
    bit_mask = ((idx - 1) << 1) + 1
    result = x | bit_mask

    return result


def mod(x, y):
    return x & (y - 1)


def is_power_of_two(x):
    return count_1_bits(x=x) == 1


# =======================================================
# Test harness
# =======================================================


# =======================================================
# Modulo of a power of two
# =======================================================

# divisor_range = range(1, 8)
# test_range = range(1, 1000)
# size = 10

# tests = random.choices(test_range, k=size)
# divisors = random.choices(divisor_range, k=size)

# for test, exponent in zip(tests, divisors):
#     result = mod(x=test, y=2**exponent)

# =======================================================
# =======================================================

# =======================================================
# Is a power of two
# =======================================================

# true_values = [2**n for n in range(2, 1000)]
# false_values = [2**n - 1 for n in range(2, 1000)]

# for success_candidate, fail_candidate in zip(true_values, false_values):
#     assert is_power_of_two(success_candidate)
#     assert not is_power_of_two(fail_candidate)

# =======================================================
# =======================================================


# =======================================================
# Parity
# =======================================================

# test_range = range(1, 10000)
# size = 1000

# tests = random.choices(test_range, k=size)

# for test in test_range:
#     print(f"\nTest value: {test:008b}")
#     reference_result = parity(x=test)
#     bit_erasure_result = parity(x=test, method="bit_erasure")
#     bit_grouping_result = parity(x=test, method="bit_grouping")

#     print(f"reference_result: {reference_result}")
#     print(f"bit_erasure_result: {bit_erasure_result}")
#     print(f"bit_grouping_result: {bit_grouping_result}")
#     print("\n------------------")

#     assert reference_result == bit_erasure_result
#     assert reference_result == bit_grouping_result

# =======================================================
# =======================================================
