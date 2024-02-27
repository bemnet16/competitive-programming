# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root.left and not root.right: return True
        elif not root.left or not root.right: return False
        ql,qr=[root.left],[root.right]
        cl,cr=root.left,root.right
        while ql and qr:
            if cl.val!=cr.val:
                return False
            if cl.left!=None and cr.right!=None:
                ql.append(cl.left)
                qr.append(cr.right)
            elif cl.left!=None or cr.right!=None:
                return False
            if cl.right!=None and cr.left!=None:
                ql.append(cl.right)
                qr.append(cr.left)
            elif cr.left!=None or cl.right!=None:
                return False
            cl=ql.pop(0)
            cr=qr.pop(0)
        return True