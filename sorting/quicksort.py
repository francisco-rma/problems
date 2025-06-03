import sys
import os
from typing import Sequence


# ANSI color codes
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"


def array_log(arr: Sequence[int], track: dict[int,]):
    arr_str = "["
    for idx, val in enumerate(arr):
        if idx in track:
            arr_str += f"{track[idx]}{val}{RESET}, "
        else:
            arr_str += f"{val}, "
    arr_str = arr_str.rstrip(", ") + "]"
    print(f"{BOLD}arr={RESET}{arr_str}")


def pretty_log(arr: Sequence[int], left: int, right: int, i: int, j: int, pivot_value: int):
    # Pretty logging for debugging with color
    print(f"{CYAN}{'=' * 40}{RESET}")
    # Print arr with color for i, j, right
    array_log(arr=arr, track={i: GREEN, j: BLUE, right: RED, left: YELLOW})
    print(
        f"{YELLOW}Left={left}, {RED}Right={right}, Pivot Value={pivot_value}{RESET}, {GREEN}Pivot Index={i}"
    )
    print(f"{GREEN}i={i},{RESET} {BLUE}j={j}{RESET}, {BLUE}arr[j]={arr[j]}{RESET}")
    print(f"{BOLD}Current subarray:{RESET} {arr[left:right+1]}")
    print(f"{RESET}Elements <= pivot:{RESET} {arr[left:i+1] if i >= left else []}")
    print(f"{CYAN}{'=' * 40}{RESET}")
    input("Press Enter to continue...")

    # Clear the terminal after input
    if os.name == "nt":
        os.system("cls")

    sys.stdout.flush()


def partition(arr: Sequence[int], left: int, right: int, debug=False) -> int:
    pivot_value = arr[right]
    i = left - 1

    for j in range(left, right):
        if debug:
            pretty_log(arr=arr, left=left, right=right, i=i, j=j, pivot_value=pivot_value)
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[right] = arr[right], arr[i]

    if debug:
        # Final state after partition
        print(f"{BOLD}{'-' * 40}{RESET}")
        print(f"{BOLD}After partition:{RESET} arr={arr}")
        print(f"{YELLOW}New pivot position: {i}{RESET}")
        print(f"{BOLD}{'-' * 40}{RESET}")

        if os.name == "nt":
            os.system("cls")

        sys.stdout.flush()

    return i


def qs(arr: Sequence[int], left: int, right: int, debug=False) -> int:
    if right - left <= 0:
        if debug:
            print("EXIT CONDITION:")
            array_log(arr=arr, track={right: RED, left: YELLOW})
            input()
            if os.name == "nt":
                os.system("cls")

            sys.stdout.flush()
        return

    pivot = partition(arr, left, right, debug=debug)
    qs(arr, left, pivot - 1, debug=debug)
    qs(arr, pivot + 1, right, debug=debug)


def quicksort(arr: Sequence[int]):
    qs(arr=arr, left=0, right=len(arr) - 1, debug=False)
    return
