

def sum_squares(n, memo=None):
	if memo is None: memo={}

	# base case
	if n == 0: return 0

	# memoized?
	if n in memo: return memo[n]

	# try all the perfect squares <= n
	i = 1
	ans = []
	while i*i <= n:
		ans.append(1 + sum_squares(n- i*i, memo))
		i += 1
	
	memo[n] = min(ans)
	return memo[n]

res = sum_squares(10)
print(res)