# iterative
def depth_first_values(root):
  if not root:
    return []
  ans = []
  stack = [root]
  while stack:
    cur = stack.pop()
    ans.append(cur.val)

    if cur.right:
      stack.append(cur.right)
    if cur.left:
      stack.append(cur.left)
  return ans


# recursive

def depth_first_values(root,ans=None):
  if not root:
    return []
  if ans == None:
    ans = []
  ans.append(root.val)
  depth_first_values(root.left,ans)
  depth_first_values(root.right,ans)
  
  
  return ans