
# dfs iterative
def tree_includes(root, target):
  if not root:
    return False
  stack = [root]
  
  while stack:
    curr = stack.pop()
    if curr.val == target:
      return True
    if curr.left:
      stack.append(curr.left)
    if curr.right:
      stack.append(curr.right)
      
  return False


# dfs recursive
def tree_includes(root, target):
  if not root:
    return False
  
  if root.val == target:
    return True
  if tree_includes(root.left,target) or tree_includes(root.right,target):
    return True
  return False


# bfs
from collections import deque 
def tree_includes(root, target):
  if not root:
    return False
  
  q = deque([root])
  
  while q:
    curr = q.pop()
    if curr.val == target:
      return True
    
    if curr.left:
      q.appendleft(curr.left)
    if curr.right:
      q.appendleft(curr.right)
      
  return False 