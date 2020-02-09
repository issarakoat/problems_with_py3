import TreeNode
import Leetcode

T1 = TreeNode.TreeNode(5)
T1.left = TreeNode.TreeNode(4)
T1.right = TreeNode.TreeNode(8)
T1.right.left = TreeNode.TreeNode(13)
T1.right.right = TreeNode.TreeNode(4)
T1.right.right.right = TreeNode.TreeNode(1)
T1.left.left = TreeNode.TreeNode(11)
T1.left.left.left = TreeNode.TreeNode(7)
T1.left.left.right = TreeNode.TreeNode(2)

_lc = Leetcode.LC()
print(_lc.isSymmetric(T1))