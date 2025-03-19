def knightAttack(N: int, position: list[int], opponents: list[list[int]], K):
    def is_reachable(source: tuple[int, int], target: tuple[int, int]) -> bool:
        result = False

        return result

    def list_moves(pos: tuple[int, int]):
        moves = []
        i, j = pos[0], pos[1]

        if i + 2 < K:
            if j + 1 < K:
                moves.append(tuple([i + 2, j + 1]))
            if j - 1 < 0:
                moves.append(tuple([i + 2, j - 1]))
        if j + 2 < K:
            if i + 1 < K:
                moves.append(tuple([i + 1, j + 2]))
            if i - 1 < 0:
                moves.append(tuple([i - 1, j + 2]))
        if i - 2 < 0:
            if j + 1 < K:
                moves.append(tuple([i - 2, j + 1]))
            if j - 1 < 0:
                moves.append(tuple([i - 2, j - 1]))
        if j - 2 < 0:
            if i + 1 < K:
                moves.append(tuple([i + 1, j - 2]))
            if i - 1 < 0:
                moves.append(tuple([i - 1, j - 2]))
        return moves

    visited_positions: set[tuple[int, int]] = set()
    capturable_opponents: dict[int, int] = {}

    move_count = 0

    i, j = position[0], position[1]

    while move_count < K:
        moves = list_moves((i, j))
        for opponent in opponents:
            if opponent in moves and opponent not in visited_positions:
                if move_count not in capturable_opponents:
                    capturable_opponents[move_count] = 1
                else:
                    capturable_opponents[move_count] += 1

        for move in moves:
            visited_positions.add(move)

        move_count += 1

    max_captures = 0
    for key, val in capturable_opponents.items():
        if val != 0:
            max_captures += 1

    return max_captures
