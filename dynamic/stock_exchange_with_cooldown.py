from functools import lru_cache


def maxProfit(prices: list[int]) -> int:
    @lru_cache(None)
    def max_profit_recursive(idx: int, holding: bool):
        if idx >= len(prices):
            return 0

        # holding
        if holding:
            # sell
            sell = prices[idx] + max_profit_recursive(idx + 2, False)
            # don't sell
            dont_sell = max_profit_recursive(idx + 1, holding)
            return max(sell, dont_sell)

        # not_holding
        else:
            # buy
            buy = -prices[idx] + max_profit_recursive(idx + 1, True)
            # don't buy
            dont_buy = max_profit_recursive(idx + 1, False)
            return max(buy, dont_buy)

    return max_profit_recursive(0, False)


prices = [1, 3, 4, 0, 4]

result = maxProfit(prices)


print(result)
