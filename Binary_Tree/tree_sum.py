# iterative dfs

def tree_sum(root):
  if not root:
    return 0
  stack = [root]
  ans = 0
  while stack:
    cur = stack.pop()
    ans += cur.val
    if cur.right:
      stack.append(cur.right)
    if cur.left:
      stack.append(cur.left)
  return ans
  

# recursive dfs
def tree_sum(root):
  if not root:
    return 0
  left = tree_sum(root.left)
  right = tree_sum(root.right)
  return left + right + root.val



# bfs
import collections
def tree_sum(root):
  if not root:
    return 0
  q = collections.deque([root])
  ans = 0
  while q:
    cur = q.pop()
    ans += cur.val
    if cur.left:
      q.appendleft(cur.left)
    if cur.right:
      q.appendleft(cur.right)
        
  return ans