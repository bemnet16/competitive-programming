# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        stc = [root]
        res = []
        while stc:
            temp = []
            for i in range(len(stc)):
                cur = stc.pop(0)
                if cur:
                    temp.append(cur.val)
                    stc.append(cur.left)
                    stc.append(cur.right)
            if temp:
                res.append(temp)
        return res[::-1]
