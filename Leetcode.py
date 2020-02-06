import TreeNode

T1 = TreeNode.TreeNode(3)
T1.left = TreeNode.TreeNode(9)
T1.right = TreeNode.TreeNode(20)
T1.right.left = TreeNode.TreeNode(15)
T1.right.right = TreeNode.TreeNode(7)

class LC:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = []
        stack.append(root)
        if root:
            check_left = root.val
            check_right = root.val
            current_val = root.val
        else: return False
        while stack != []:
            expand = stack.pop()  
            if expand.val == sum and expand.left == None and expand.right == None :
                return True
            if expand.left:
                if expand.left.val + check_left == sum:                   
                    return True                   
                elif expand.left.val + check_left < sum:                  
                    current_val = check_left
                    check_left += expand.left.val
                stack.append(expand.left)
            if expand.right:
                if expand.right.val + check_right == sum:                   
                    return True                    
                elif expand.right.val + check_right < sum:
                    current_val = check_right
                    check_right += expand.right.val
                    # print(current_val)
                stack.append(expand.right)
        return False
            

    def maxDepth_104(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth_104(root.left), self.maxDepth_104(root.right))

    def sayYo(self):
        print('yo')


