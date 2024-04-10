class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        
        landArea = 0
        def dfs(row, col):
            
            nonlocal landArea
            
            grid[row][col] = 0
            landArea += 1
            
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and grid[new_row][new_col]:
                    dfs(new_row, new_col)
        
        
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    maxArea = max(landArea, maxArea)
                    landArea = 0
        
        return maxArea
        