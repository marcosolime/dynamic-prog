


def counting_change(n, coins, i, memo=None):
	if memo is None: 
		memo = {}

	if n == 0: return 1
	if n < 0: return 0
	if i == len(coins): return 0

	# memoized?
	if (n,i) in memo: return memo[(n,i)]

	j = 0
	ans = 0
	while True:
		diff = n - coins[i] * j # we take j times coins[i]
		if diff < 0: break
		
		ans += counting_change(diff, coins, i+1, memo)
		j += 1

	memo[(n,i)] = ans
	return ans


ans = counting_change(4, [1,2,3], 0)
print(ans)