def trap(height: list[int]) -> int:
    max_area = 0

    left = 0
    right = len(height) - 1

    max_left = height[left]
    max_right = height[right]

    while left < right:
        if max_left <= max_right:
            left += 1
            if height[left] <= max_left:
                max_area += max(0, min(max_left, max_right) - height[left])
        else:
            right -= 1
            if height[right] <= max_right:
                max_area += max(0, min(max_left, max_right) - height[right])

        max_left = max(max_left, height[left])
        max_right = max(max_right, height[right])

    return max_area


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

max_area = trap(height)

print(max_area)
