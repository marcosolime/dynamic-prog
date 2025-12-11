

# tribonacci sequence
# trib(n) = trib(n-1) + trib(n-2) + trib(n-3)
# trib(0) -> 0
# trib(1) -> 0
# trib(2) -> 1

def trib(n, memo):
    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 1

    if n in memo: return memo[n]

    ans = trib(n-1, memo) + trib(n-2, memo) + trib(n-3, memo)
    memo[n] = ans
    return ans

out = trib(80, {})
print(out)