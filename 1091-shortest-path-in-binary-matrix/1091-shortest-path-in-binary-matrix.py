class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        level = [(0, 0)] if not grid[0][0] else []
        visited = set((0, 0))
        path = 0
        
        
        while level:
            
            next_level = []
            path += 1
            
            for row, col in level:
                
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return path
                
                for row_change, col_change in DIRECTIONS:
                    
                    new_row = row + row_change
                    new_col = col + col_change
                    
                    if inbound(new_row, new_col) and not((new_row, new_col) in visited or grid[new_row][new_col]):
                        visited.add((new_row, new_col))
                        next_level.append((new_row, new_col))
                        
            level = next_level
                     
        
        return -1
                        
                        
                        
                        
                        
                        
                        