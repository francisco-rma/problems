def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    left = 0
    right = len(matrix) * len(matrix[0]) - 1

    while left <= right:
        idx = left + ((right - left) // 2)
        row_idx, col_idx = divmod(idx, len(matrix[0]))

        if matrix[row_idx][col_idx] == target:
            return True
        elif matrix[row_idx][col_idx] > target:
            right = idx - 1
        else:
            left = idx + 1

    return False


matrix = [[1]]
target = 3

result = searchMatrix(matrix=matrix, target=target)
print(result)
