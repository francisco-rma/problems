import urllib.request
import pandas as pd


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
            d[i][j] = min(var1, var2, var3)

    return d[m][n]


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


word1 = "dinitrophenylhydrazine"
word2 = "acetylphenylhydrazine"

result = lev(word1, word2)

print(result)
