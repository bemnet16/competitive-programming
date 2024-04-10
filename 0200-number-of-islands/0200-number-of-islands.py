class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        
        def dfs(row, col):
            
            if grid[row][col] == "0":
                return
            
            
            grid[row][col] = "0"
            for row_change, col_change in DIRECTIONS:
                
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)
            
            
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
         
        return islands