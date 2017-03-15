output = list()
def tree (inorder,order):
  global output
  root = order[0]
  root_position = inorder.index(root)
  left = inorder[:root_position]
  left_order = order[1:len(left)+1]
  right = inorder[root_position+1:]
  right_order = order[-len(right):]
  if(len(left)>1 and len(left_order)>1):
    tree(left,left_order)
  if(len(right)>1 and len(right_order)>1):
    tree(right,right_order)
  output.append({inorder:[left,right,root]})
  return output

#tree("dbeafc","abdecf")
tree("0123456789","7103254698")


