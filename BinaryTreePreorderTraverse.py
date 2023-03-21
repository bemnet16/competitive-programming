### Recursiion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root):
        if root:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res

 #### Iteration

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        stc = [root]
        res = []
        s = root
        while stc:
            if s:
                stc.append(s)
                res.append(s.val)
                s = s.left
            else:
                if len(stc) > 1:
                    s = stc.pop().right
                else:
                    stc = []
        return res
