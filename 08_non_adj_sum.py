

"""
def non_adjacent_sum(numbers, memo=None):
    if memo is None: memo = {}
    if numbers == []: return 0

    # already memoized
    if tuple(numbers) in memo:
        return memo[tuple(numbers)]

    sums = []
    # pick the first number...
    sums.append(numbers[0] + non_adjacent_sum(numbers[2:], memo))
    # or skip it
    sums.append(non_adjacent_sum(numbers[1:], memo))

    val = max(sums)
    memo[tuple(numbers)] = val
    return val
"""

# more efficient -> uses indexes and not list slicing
def non_adjacent_sum(numbers, i=0, memo=None):
    if memo is None:
        memo = {}

    if i >= len(numbers):
        return 0
    
    if i in memo:
        return memo[i]

    include = numbers[i] + non_adjacent_sum(numbers, i+2, memo)
    exclude = non_adjacent_sum(numbers, i+1, memo)

    memo[i] = max(include, exclude)
    return memo[i]


numbers = [2,4,7,1,4,1,2]
ans = non_adjacent_sum(numbers)
print(ans)