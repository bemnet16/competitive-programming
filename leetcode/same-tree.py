# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not(p or q): return True
        elif not(p and q): return False
        p_que=[p]
        q_que=[q]
        while p_que and q_que:
            p_cur=p_que.pop(0)
            q_cur=q_que.pop(0)
            if p_cur.val != q_cur.val:
                return False
            if p_cur.left and q_cur.left:
                p_que.append(p_cur.left)
                q_que.append(q_cur.left)
            elif p_cur.left or q_cur.left:
                return False
            if p_cur.right and q_cur.right:
                p_que.append(p_cur.right)
                q_que.append(q_cur.right)
            elif p_cur.right or q_cur.right:
                return False
        if not(p_que or q_que):
            return True
        return False