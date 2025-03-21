import urllib.request
import pandas as pd

from utils import decorators


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


def lev(p: str, q: str) -> int:
    m = len(p)
    n = len(q)
    d: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    substitution_cost: int = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[i - 1] == q[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            var1 = d[i - 1][j] + 1
            var2 = d[i][j - 1] + 1
            var3 = d[i - 1][j - 1] + substitution_cost

            # print(f"\nDeletion: {var1}")
            # print(f"Insertion: {var2}")
            # print(f"Substitution: {var3}")

            d[i][j] = min(var1, var2, var3)
            # print(f"Result: {d[i][j]}\n")

    # print(p, "  ", q)
    # for row in d:
    #     print(row)
    return d[m][n]


@decorators.print_runtime
def random_words(size=100):

    path = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = urllib.request.urlopen(url=path)
    words = response.read().decode().splitlines()

    results: list[tuple[str, str, int]] = []
    computed_pairs: set[tuple[str, str]] = []

    assert size < len(words)

    print(f"\nSIZE: {size}")

    for _, source in enumerate(words[:size]):
        for _, target in enumerate(words[:size]):
            pair = tuple([source, target])
            if target == source or pair in computed_pairs:
                continue

            dist = lev(source, target)
            results.append(tuple([source, target, dist]))

    df: pd.DataFrame = pd.DataFrame(results)
    df.to_csv("results.csv")
