

def max_path(x, y, grid, memo=None):
    rows, cols = len(grid), len(grid[0])
    
    if memo is None: memo = {}

    # reached goal
    if x == rows-1 and y == cols-1:
        return grid[x][y]

    # already memoized
    if (x,y) in memo: return memo[(x,y)]

    # visit 2 directions
    sums = []
    if x+1 < rows:
        sums.append(max_path(x+1, y, grid, memo))
    if y+1 < cols:
        sums.append(max_path(x, y+1, grid, memo))
    
    # add myself
    val = max(sums) + grid[x][y]

    # memoize it
    memo[(x,y)] = val
    return val

grid = [
    [2,4,5,6,2],
    [2,5,1,4,1],
    [2,7,8,6,2],
    [3,1,1,1,2]
]

ans = max_path(0, 0, grid)
print(ans)