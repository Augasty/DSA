def island_count(grid):
  visited = set()
  size = len(grid)*len(grid[0])
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      pos = str(r)+','+str(c)
      if grid[r][c] == 'L' and pos not in visited:
        currSize = 0
        size = min(size,explore(grid,r,c,visited, currSize))
  return size

def explore(grid,r,c,visited,currSize):
  pos = str(r)+','+str(c)
  if grid[r][c] == 'L' and pos not in visited:
    visited.add(pos)
    currSize += 1
    # print(pos)
    if r > 0:
      currSize = explore(grid,r-1,c,visited,currSize)
    if r < len(grid)-1:
      currSize = explore(grid,r+1,c,visited,currSize)
    
        
    if c > 0:
      currSize = explore(grid,r,c-1,visited,currSize)
    if c < len(grid[0])-1:
      currSize = explore(grid,r,c+1,visited,currSize)

    return currSize
  else:
    return currSize
    
    
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid))