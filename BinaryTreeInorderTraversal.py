#### Recursion

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

    
    
    ### Iterative way
    
    
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
        if not root:
            return []
        stc = [root]
        res = []
        s = root
        while stc:
            if s:
                stc.append(s)
                s = s.left
            else:
                cur = stc.pop()
                if cur:
                    res.append(cur.val)
                    s = cur.right
                else:
                    if len(stc) == 1:
                        stc = []
        res.pop()
        return res
