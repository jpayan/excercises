"""
[EASY]
This problem was asked by Facebook

Given an array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""


def get_maximum_profit(price_history: list) -> int:
    n = len(price_history)
    max_profit = 0
    i = 0
    j = 1
    if n > 0:
        while i < n - 1:
            profit = price_history[j] - price_history[i]
            max_profit = max(profit, max_profit)
            j += 1
            if j == n:
                i += 1
                j = i + 1
    return max_profit

assert get_maximum_profit([9, 11, 8, 5, 7, 10]) == 5
assert get_maximum_profit([11, 10, 9, 8, 7, 6, 5]) == 0
assert get_maximum_profit([5, 6, 7, 8, 9, 10, 11]) == 6
assert get_maximum_profit([1]) == 0
assert get_maximum_profit([1, 1]) == 0