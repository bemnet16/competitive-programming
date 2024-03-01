class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        max_rows = [-1] * n
        max_cols = [-1] * n
        
        for i in range(n):
            for j in range(n):
                
                max_rows[i] = max(max_rows[i], grid[i][j])
                max_cols[i] = max(max_cols[i], grid[j][i])
        
        
        max_sum = 0
        
        for i in range(n):
            for j in range(n):
                
                max_sum += (min(max_rows[i], max_cols[j]) - grid[i][j])
        
        
        return max_sum
                
                
            
        