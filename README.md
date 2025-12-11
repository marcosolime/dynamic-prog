# dynamic-prog
A set of exercises solved using dynamic programming

## what is dynamic programming?
DP = solving a big problem by solving smaller overlapping subproblems once, storing their answers, and reusing them.

There are two main styles:
1. Top-down DP (*memoization*)
- you start from the original problem (`fib(n)`)
- you recursively ask for subproblems
- when you compute a value once, you save it
- the next time you need it, you reuse it ($O(1)$ lookup)

2. Bottom-up DP (*tabulation*)
- you build solutions from smallest subproblems upward
- no recursion (!); we fill a table/array iteratively

```python
def fib(n):
    dp = [0, 1]
    for _ in range(2, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]
```

*Note: if we cache results of overlapping subproblems, we are doing DP.*