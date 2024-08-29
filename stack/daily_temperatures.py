def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    result = [0] * len(temperatures)

    i = 0

    while i <= len(temperatures) - 1:
        current_temp = temperatures[i]

        if not stack or current_temp <= temperatures[stack[-1]]:
            stack.append(i)
            i += 1
            continue

        while stack and current_temp > temperatures[stack[-1]]:
            result[stack[-1]] = i - stack[-1]
            stack.pop()

        stack.append(i)
        i += 1

    return result


temperatures = [30, 40, 50, 60]

result = dailyTemperatures(temperatures=temperatures)

print(result)
