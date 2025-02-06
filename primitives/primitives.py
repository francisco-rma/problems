def count_1_bits(x) -> int:
    count = 0
    while x:
        print("\nx is    : {0:03d} ({0:07b})".format(x))
        print("1 is    : {0:03d} ({0:07b})".format(1))
        print("x & 1 is: {0:03d} ({0:07b})".format(x & 1))
        count += x & 1
        print(f"count is: {count}\n")
        x >>= 1

    return count


def parity(x, method: str = "bruteforce"):
    match method:
        case "bruteforce":
            result = 0
            while x:
                print("\nx is    : {0:03d} ({0:07b})".format(x))
                print("1 is    : {0:03d} ({0:07b})".format(1))
                print("x & 1 is: {0:03d} ({0:07b})".format(x & 1))
                result ^= x & 1
                x >>= 1
            return result

        case "bit_erasure":
            result = 0
            while x:
                print("\nx is     : {0:03d} ({0:07b})".format(x))
                result ^= 1
                print("result is: {0:03d} ({0:07b})".format(result))
                x &= x - 1
            return result

        case "bit_grouping":
            bit_count = len(str(bin(x))[2:])
            while bit_count:
                bit_count >>= 1
                print("\ngroup size is: {0:03d} ({0:08b})".format(bit_count))
                print("x is         : {0:03d} ({0:08b})".format(x))
                x ^= x >> (bit_count)

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

    print("\nx is       : {0:06d} ({0:08b})".format(x))
    print("bit mask is: {0:06d} ({0:08b})".format(bit_mask))
    print("result is  : {0:06d} ({0:08b})".format(result))

    return result


# =======================================================
# Test cases
# =======================================================

test = "11010000"
result = right_propagate(int(test, base=2))

print(f"Result is: {result}")
