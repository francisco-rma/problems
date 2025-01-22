from collections import deque


class Solution:
    def boustrophedon_position(self, number, cols):
        adjusted_number = number - 1
        i = adjusted_number // cols
        if i % 2 == 0:
            j = adjusted_number % cols
        else:
            j = cols - 1 - (adjusted_number % cols)
        return cols - i - 1, j

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        n_square = n**2

        queue = deque()
        queue.append((1, 0))

        visited = set()
        visited.add(1)

        while queue:
            current_square, num_dices = queue.popleft()

            if current_square == n_square:
                return num_dices

            for next_position in range(
                current_square + 1, min(current_square + 6, n_square) + 1
            ):
                if next_position not in visited:
                    next_i, next_j = self.boustrophedon_position(next_position, n)
                    next_number_on_position = board[next_i][next_j]

                    visited.add(next_position)

                    if next_number_on_position != -1:
                        queue.append((next_number_on_position, num_dices + 1))
                        # visited.add(next_number_on_position)
                    else:
                        queue.append((next_position, num_dices + 1))

        return -1


board = [
    [-1, -1, -1, 46, 47, -1, -1, -1],
    [51, -1, -1, 63, -1, 31, 21, -1],
    [-1, -1, 26, -1, -1, 38, -1, -1],
    [-1, -1, 11, -1, 14, 23, 56, 57],
    [11, -1, -1, -1, 49, 36, -1, 48],
    [-1, -1, -1, 33, 56, -1, 57, 21],
    [-1, -1, -1, -1, -1, -1, 2, -1],
    [-1, -1, -1, 8, 3, -1, 6, 56],
]
sol = Solution()

result = sol.snakesAndLadders(board=board)

print(result)
