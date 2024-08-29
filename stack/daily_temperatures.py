def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temperatures)

    for idx, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            result[stack[-1]] = idx - stack[-1]
            stack.pop()

        stack.append(idx)

    return result


temperatures = [30, 40, 50, 60]

result = dailyTemperatures(temperatures=temperatures)

print(result)
