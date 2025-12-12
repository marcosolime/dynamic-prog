from typing import List

def min_change(amount: int, coins: List[int], memo=None):
    if memo is None:
        memo = {}

    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')  # impossible path

    if amount in memo:
        return memo[amount]

    min_coins = float('inf')

    for c in coins:
        attempt = 1 + min_change(amount - c, coins, memo)
        min_coins = min(min_coins, attempt)

    memo[amount] = min_coins
    return min_coins

# Testing
print(min_change(5, [1,2,3]))   # -> 2 (2+3 or 1+1+3)
