


def max_change(amount, coins, memo=None):
    if memo is None:
        memo = {}
    if amount <= 0: return 0
    if amount in memo:
        return memo[amount]

    max_val = float('-inf')
    for c in coins:
        if amount-c >= 0:
            val = 1 + max_change(amount-c, coins, memo)
            if val > max_val:
                max_val = val
    
    memo[amount] = max_val
    return max_val

ans = max_change(5, [1,5,3,2,6])
print(ans)