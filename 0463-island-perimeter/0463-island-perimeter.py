class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        VISITED = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        
        def inbound(row, col):
            
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        
        perimeter = 0
        def dfs(row, col):
            
            nonlocal perimeter
            
            if not grid[row][col]:
                perimeter += 1
                return
            
            
            VISITED[row][col] = True
            
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                bounded = inbound(new_row, new_col)
                
                if bounded and not VISITED[new_row][new_col]:
                    dfs(new_row, new_col)
                
                elif not bounded:
                    perimeter += 1
        

        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    dfs(row, col)
                    return perimeter
    
    
    
    
    
    
    
    
    
    
    