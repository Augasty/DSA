def max_path_sum(root):
  if not root:
    return float('-inf')
  if not root.left and not root.right:
    return root.val

  left = max_path_sum(root.left)
  right = max_path_sum(root.right)
  
  path = max(left,right)
  
  return path + root.val