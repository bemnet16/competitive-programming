# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        stc = [root]
        result = []
        while stc:
            temp = []
            for i in range(len(stc)):
                cur = stc.pop()
                if cur:
                    temp.append(cur.val)
                    stc.insert(0,cur.left)
                    stc.insert(0,cur.right)
            if temp:
                result.append(temp)
        return result

    
