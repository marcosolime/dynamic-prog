
# solving fibonacci with memoization
# n: input size
# time complexity: O(n)
# space complexity: O(n)

def fib(n, memo):
    # base cases
    if n == 0: return 0
    if n == 1: return 1
    if n in memo: return memo[n]

    ans = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = ans
    return ans

out = fib(800, {})
print(out)
