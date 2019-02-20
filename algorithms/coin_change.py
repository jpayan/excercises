# This problem was asked by Google.
# Find the minimum number of coins required to make n cents.
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
from typing import List


# Greedy (Works due to currency)
def get_least_coins(denomination: List[int], amount: int) -> int:
    coins = 0
    for coin in sorted(denomination, reverse=True):
        coins += amount // coin
        amount = amount % coin
    return coins


if __name__ == '__main__':
    denomination = [1, 5, 10, 25]
    amount = 16
    print(get_least_coins(denomination, amount))
