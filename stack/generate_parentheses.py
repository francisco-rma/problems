def generateParenthesis(n: int) -> list[str]:
    """ """
    res = []

    def dfs(left: int, right: int, value: str):
        if len(value) == n * 2:
            res.append(value)

        if left < n:
            dfs(left + 1, right, value + "(")

        if right < left:
            dfs(left, right + 1, value + ")")

    dfs(0, 0, "")
    return res


n = 3

test = generateParenthesis(n)

print(test)
