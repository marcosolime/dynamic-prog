

def edit(word1, word2, i, j, memo=None):
	if memo is None: memo = {}

	# base cases
	if i == len(word1):
		return len(word2)-j
	if j == len(word2):
		return len(word1)-i

	# memoized?
	if (i,j) in memo: return memo[(i,j)]
	
	if word1[i] == word2[j]: # no op!
		memo[(i,j)] = edit(word1, word2, i+1, j+1, memo)
		return memo[(i,j)]

	# different -> try 3 operations
	ops = []
	ops.append(1 + edit(word1, word2, i+1, j, memo)) # del
	ops.append(1 + edit(word1, word2, i, j+1, memo)) # ins
	ops.append(1 + edit(word1, word2, i+1, j+1, memo)) # rep

	memo[(i,j)] = min(ops)
	return memo[(i,j)]

ans = edit("marco", "xxrcoo", 0, 0)
print(ans)