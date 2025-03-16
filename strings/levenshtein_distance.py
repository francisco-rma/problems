def levenshtein_distance(p: str, q: str) -> int:
    if len(p) == 0:
        return len(q)

    elif len(q) == 0:
        return len(p)

    elif p[0] == q[0]:
        return levenshtein_distance(p[1:], q[1:])

    else:
        return 1 + min(
            levenshtein_distance(p[1:], q),
            levenshtein_distance(p, q[1:]),
            levenshtein_distance(p[1:], q[1:]),
        )

    ...
