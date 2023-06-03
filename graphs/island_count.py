def island_count(grid):
  visited = set()
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      pos = str(r)+str(c)
      if grid[r][c] == 'L' and pos not in visited:
        explore(grid,r,c,visited)  
        count += 1
  return count

def explore(grid,r,c,visited):
  pos = str(r)+str(c)
  if grid[r][c] == 'L' and pos not in visited:
    visited.add(pos)
    print(pos)
    if r > 0:
      explore(grid,r-1,c,visited)
    if r < len(grid)-1:
      explore(grid,r+1,c,visited)
    
        
    if c > 0:
      explore(grid,r,c-1,visited)
    if c < len(grid[0])-1:
      explore(grid,r,c+1,visited)
  else:
    return True
    
    
# grid = [
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'W', 'W', 'L', 'W'],
#   ['W', 'W', 'L', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['L', 'L', 'W', 'W', 'W'],
# ]

# print(island_count(grid))