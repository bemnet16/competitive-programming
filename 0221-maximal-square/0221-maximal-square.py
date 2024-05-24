class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        def check(row, col):
            if (0 <= row < m) and (0 <= col < n):
                return int(matrix[row][col])
            return 0
        
        
        max_side = 0
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                
                if matrix[row][col] == "0":
                    matrix[row][col] = 0
                    continue
                
                right = check(row, col + 1)
                diagonal = check(row + 1, col + 1)
                down = check(row + 1, col)
                
                matrix[row][col] = 1 + min(right, diagonal, down)
                max_side = max(max_side, matrix[row][col])
                
        return max_side * max_side