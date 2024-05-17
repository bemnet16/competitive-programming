class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        
        
        def check(row, col):
            if (0 <= row < m) and (0 <= col < n):
                return dp[row][col]
            return 0
        
        
        for row in range(m):
            for col in range(n):
                
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                
                else:
                    dp[row][col] += (check(row - 1, col) + check(row, col - 1))
        
        
        return dp[-1][-1]