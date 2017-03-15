import pprint
pp = pprint.PrettyPrint(indent = 4)
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
  output.append({(inorder,root):[left,right]})
  return output

pp.pprint(tree("0123456789","7103254698"))

for i in range(0,len(output)):
  [v] = list(output[i].values())
  [k] = list(output[i].keys())
  print("inorder",k[0],"root",k[1],"left",v[0],"right",v[1])