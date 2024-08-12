class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        if m * n <= 2:
            return False
        

        def dfs(row, col):
            
            if row >= m or col >= n:
                return False
            
            if row == m - 1 and col == n - 1:
                return True
            
            if grid[row][col] == 0:
                return False
            
            grid[row][col] = 0
            
            if dfs(row + 1, col) or dfs(row, col + 1):
                return True
        
        
        
        return  not (dfs(1, 0) and dfs(0, 1))