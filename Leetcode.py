import TreeNode

T1 = TreeNode.TreeNode(3)
T1.left = TreeNode.TreeNode(9)
T1.right = TreeNode.TreeNode(20)
T1.right.left = TreeNode.TreeNode(15)
T1.right.right = TreeNode.TreeNode(7)

class LC:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = []
        left = -1
        right = -1
        if root:
            current_val = root.val
            print('root ', current_val)
            stack.append((root,current_val))
        else: 
            return False
        while stack != []:
            expand = stack.pop()  
            current_node = expand[0]
            current_val = expand[1]
            if current_val == sum and current_node.left == None and current_node.right == None :
                return True
            if current_node.left:                                
                left = current_val + current_node.left.val
                print('left :', left)
                stack.append((current_node.left, left))
            if current_node.right:                   
                right = current_val + current_node.right.val
                print('right :', right)
                stack.append((current_node.right, right))
        return False
            

    def maxDepth_104(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth_104(root.left), self.maxDepth_104(root.right))

    def sayYo(self):
        print('yo')


