# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        # track values that have the same columns
        self.col_track = defaultdict(list)
        
    def vertical(self, root):
        
        if root:
            val, row, col = root.val
            self.col_track[col].append([row, val])
            
            if root.left:
                root.left.val = (root.left.val, row + 1, col - 1)
                self.vertical(root.left)
            
            if root.right:
                root.right.val = (root.right.val, row + 1, col + 1)
                self.vertical(root.right)
                
        return root
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        root.val = (root.val, 0, 0)
        self.vertical(root)
        
        cols = list(self.col_track.items())
        cols.sort()
        
        answer = []
        
        for col,vals in cols:
            values = sorted(vals, key = lambda x: (x[0], x[1]))
            index_1_values = [item[1] for item in values]
            answer.append(index_1_values)
        
        return answer
        
       
        
