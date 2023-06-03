import collections

def breadth_first_values(root):
  if root == None:
    return []
  q = collections.deque([root])
  ans = []
  while q:
    cur = q.pop()
    ans.append(cur.val)
    if cur.left:
      q.appendleft(cur.left)
    if cur.right:
      q.appendleft(cur.right)
      
  return ans