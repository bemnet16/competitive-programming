class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        cache = {}
        
        def inbound(row, col):
            return (0 <= row < len(matrix)) and (0 <= col < len(matrix[0]))
        
        def dp(row, col):
            
            if not inbound(row, col):
                return 0
            
            if (row, col) in cache:
                return cache[(row, col)]
            
            
            left = 1
            if inbound(row, col + 1) and matrix[row][col] < matrix[row][col + 1]:
                left = 1 + dp(row, col + 1)
                
            right = 1
            if inbound(row, col - 1) and matrix[row][col] < matrix[row][col - 1]:
                right = 1 + dp(row, col - 1)
                
            up = 1
            if inbound(row - 1, col) and matrix[row][col] < matrix[row - 1][col]:
                up = 1 + dp(row - 1, col)
                
            down = 1
            if inbound(row + 1, col) and matrix[row][col] < matrix[row + 1][col]:
                down = 1 + dp(row + 1, col)
            
            
            cache[(row, col)] = max(left, right, up, down)
            
            return cache[(row, col)]
        
        
        long_path = 1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                long_path = max(long_path, dp(row, col))
                
        return long_path
            
        