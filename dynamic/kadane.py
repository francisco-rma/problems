def largest_sum(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise ValueError("Empty list")

    i = 1
    min_idx = 0
    max_sum = numbers[0]
    current_sum = numbers[0]
    window = [0, 0]

    while i < len(numbers):
        current_sum = max(current_sum + numbers[i], numbers[i])
        if current_sum == numbers[i]:
            min_idx = i

        max_sum = max(current_sum, max_sum)
        if max_sum == current_sum:
            window[0], window[1] = min_idx, i

        i += 1

    return max_sum, window


array = [4, -1, 2, -7, 3, 4]
result, window = largest_sum(array)
print(f"Largest sum: {result}")
print(f"Window: {window}")
print(f"Window value: {array[window[0]:window[1]+1]}")
