def largest_sum(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise ValueError("Empty list")

    max_sum = 0
    current_sum = 0

    min_idx = 0
    max_idx = 0

    L = 0

    for R, value in enumerate(numbers):
        current_sum = max(current_sum + value, value)
        if current_sum == value:
            L = R

        max_sum = max(current_sum, max_sum)
        if max_sum == current_sum:
            min_idx, max_idx = L, R

    return max_sum, (min_idx, max_idx)


array = [4, -1, 2, -7, 3, 4]
result, window = largest_sum(array)
print(f"Largest sum: {result}")
print(f"Window: {window}")
print(f"Window value: {array[window[0]:window[1]+1]}")
