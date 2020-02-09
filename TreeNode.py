# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def insert(self, num):
        if self.val:
            if num < self.val:
                if self.left is None:
                    self.left = TreeNode(num)
                else:
                    self.left.insert(num)
            elif num >= self.val:
                if self.right is None:
                    self.right = TreeNode(num)
                else:
                    self.right.insert(num)
        else:
            self.val = num

    #print the sorted
    def print_preorder(self):       
        if self.left:
            self.left.print_preorder()   
        print( self.val)     
        if self.right:
            self.right.print_preorder()
    #6 2 1 4 3 5 7 9 8
    def print_inorder(self):
        print( self.val)
        if self.left:
            self.left.print_inorder()       
        if self.right:
            self.right.print_inorder()
    #1 3 5 4 2 8 9 7 6
    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.val)

def preorderList(root: TreeNode):
    stack = []
    res = []
    if root:
        stack.append(root)
    else: return res
    while stack != []:
        expand = stack.pop()
        res.append(expand.val)
        if expand.right:
            stack.append(expand.right)
        if expand.left:
            stack.append(expand.left)

    return res
def inorderList(root: TreeNode):
    stack = []
    res = []
    p = root
    while stack != [] or p != None:
        if p:
            stack.append(p)
            p = p.left
        else:
            expand = stack.pop()
            res.append(expand.val)
            p = expand.right

    return res
def postorderList(root: TreeNode):
    stack = []
    res = []
    p = root
    while stack != [] or p != None:
        if p:
            stack.append(p)
            res.insert(0,p.val)
            p = p.right
        else:
            expand = stack.pop()
            
            p = expand.left

    return res

                