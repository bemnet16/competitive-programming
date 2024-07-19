class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        minRows = [float('inf') for _ in range(m)]
        maxCols = [float('-inf') for _ in range(n)]
        
        for row in range(m):
            for col in range(n):
                minRows[row] = min(minRows[row], matrix[row][col])
                maxCols[col] = max(maxCols[col], matrix[row][col])
                

        ans = []
        for row in range(m):
            for col in range(n):
                val = matrix[row][col]
                if val == minRows[row] and val == maxCols[col]:
                    ans.append(val)
        
        
        return ans