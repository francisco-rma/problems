def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0
    for idx, val in enumerate(heights):
        effective_index = idx

        while stack and val < stack[-1][1]:
            top = stack.pop()
            effective_index = top[0]
            size = idx - top[0]

            max_area = max(max_area, top[1] * size)

        stack.append((effective_index, val))

    while stack:
        top = stack.pop()
        size = len(heights) - top[0]
        max_area = max(max_area, top[1] * size)

    return max_area


heights = [7, 1, 7, 2, 2, 4]

result = largestRectangleArea(heights=heights)

print(result)
