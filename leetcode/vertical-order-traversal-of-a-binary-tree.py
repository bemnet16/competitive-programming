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
            
            # save nodes row and val that are on the same cols
            self.col_track[col].append([row, val])
            
            if root.left:
                root.left.val = (root.left.val, (row + 1), (col - 1))
                self.vertical(root.left)
            
            if root.right:
                root.right.val = (root.right.val, (row + 1), (col + 1))
                self.vertical(root.right)
                
        return root
    
    
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # update the root val to control its cols and rows
        root.val = (root.val, 0, 0)
        
        self.vertical(root)
        
        # sort based on columns in an ascending order
        cols = list(self.col_track.items())
        cols.sort()
        
        
        answer = []
        
        for col,row_vals in cols:
            
            # sort row-val lists of cols first based on there row number then by there actual values
            row_val = sorted(row_vals, key = lambda x: (x[0], x[1]))
            
            # extract only the node value from row-val list
            values = [val for row,val in row_val]
            
            answer.append(values)
        
        return answer
        
       
        
