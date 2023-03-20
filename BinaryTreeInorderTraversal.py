# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.l = []
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            self.l.append(root.val)
            self.inorderTraversal(root.right)
        return self.l 
