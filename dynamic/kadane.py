def largest_sum(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise ValueError("Empty list")

    i = 1
    max_sum = numbers[0]
    current_sum = numbers[0]

    while i < len(numbers):
        current_sum = max(current_sum + numbers[i], numbers[i])
        max_sum = max(current_sum, numbers[i], max_sum)
        i += 1

    return max_sum


array = [4, -1, 2, -7, 3, 4]
result = largest_sum(array)
print(f"Largest sum: {result}")
