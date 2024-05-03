class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        DIRECTIONS = [(0, 1),(0, -1), (-1, 0), (1, 0)]
        
        def inBound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        
        def dfs(row, col):
            
            nonlocal countFish
            
            countFish += grid[row][col]
            grid[row][col] = 0
            
            for row_change, col_change in DIRECTIONS:
                
                new_row = row_change + row
                new_col = col_change + col
                
                if inBound(new_row, new_col) and grid[new_row][new_col] != 0:
                    dfs(new_row, new_col)
            
            
        numFish = 0
        countFish = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    countFish = 0
                    dfs(row, col)
                    numFish = max(numFish, countFish)
        
        return numFish
        