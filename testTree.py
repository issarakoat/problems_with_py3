import TreeNode

tree = TreeNode.TreeNode(6)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.insert(5)
tree.insert(9)
tree.insert(8)
# tree.print_inorder()
# print("#########################################")
# tree.print_preorder()
# print("#########################################")
# tree.print_preorder()

print('preorder : ', TreeNode.preorderList(tree))
print('inorder :' ,TreeNode.inorderList(tree))
print('postorder :' ,TreeNode.postorderList(tree))
