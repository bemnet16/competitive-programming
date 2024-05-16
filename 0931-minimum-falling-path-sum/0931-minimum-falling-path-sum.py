class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        
        def check(row, col):
            if (0 <= row < n) and (0 <= col < n):
                return matrix[row][col]
            return float("inf")
        
        
        for row in range(n - 2, -1, -1):
            for col in range(n):
                
                matrix[row][col] += min(check(row + 1, col - 1), check(row + 1, col), check(row + 1, col + 1))
        
        
        return min(matrix[0])
                    
                
        