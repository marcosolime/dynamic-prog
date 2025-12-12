"""
Couting the number of paths to go from position (0,0)
to position (rows-1, cols-1) using DP.
"""

def count_paths(x, y, grid, memo=None):
    if memo is None: memo = {}
    rows, cols = len(grid), len(grid[0])
    
    # blocked cell?
    if grid[x][y] == 'X': return 0

    # reached goal
    if x == rows-1 and y == cols-1:
        return 1

    if (x,y) in memo:
        return memo[(x,y)]

    paths = 0

    # go down
    if x+1 != rows and grid[x+1][y] != 'X':
        paths += count_paths(x+1, y, grid, memo)
    
    # go right
    if y+1 != cols and grid[x][y+1] != 'X':
        paths += count_paths(x, y+1, grid, memo)
 
    memo[(x,y)] = paths
    return paths

grid = [
    ['.', '.', '.', 'X'],
    ['.', 'X', '.', 'X'],
    ['.', '.', '.', '.'],
    ['X', '.', '.', '.']
]

ans = count_paths(0, 0, grid)
print(ans)
