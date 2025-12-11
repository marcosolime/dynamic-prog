def sum_possible(amount, numbers, memo=None):
    if memo is None:
        memo = {}
    
    # base cases
    if amount == 0:
        return True
    if amount < 0:
        return False
    if amount in memo:
        return memo[amount]

    for num in numbers:
        if sum_possible(amount - num, numbers, memo):
            memo[amount] = True
            return True

    # we tried all the subproblems...
    memo[amount] = False
    return False

# test
print(sum_possible(15, [4, 6, 10]))
