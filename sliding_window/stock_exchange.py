def maxProfit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0

    max_profit = 0
    min_price = float("inf")

    for idx, val in enumerate(prices):
        min_price = min(min_price, prices[idx])
        max_profit = max(max_profit, prices[idx] - min_price)

    return max_profit


prices = [2, 1, 2, 1, 0, 1, 2]

result = maxProfit(prices=prices)

print(result)
