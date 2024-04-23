class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        
        level = []
        visited = set()
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    visited.add((row, col))
                    level.append((row, col))
        
        
        near = 1 
        
        while level:
            
            next_level = []
            
            for row, col in level:
                
            
                for row_change, col_change in DIRECTIONS:
                    
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                        mat[new_row][new_col] = near
                        visited.add((new_row, new_col))
                        next_level.append((new_row, new_col))
            
            near += 1
            if next_level:
                level = next_level
            else:
                break
        
        return mat
                        
                    
                    
                
                
        
        
        
        
