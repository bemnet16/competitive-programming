class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        
        def getVal(r, c):
            if (0 <= r < rows) and (0 <= c < cols):
                return matrix[r][c]
            return 0
        
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] += (getVal(r - 1, c) + getVal(r, c - 1) - getVal(r - 1, c - 1))
            
        
          
        ans = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                prefix = defaultdict(int)
                prefix[0] = 1
                for c in range(cols):
                    ans += prefix[(getVal(r2, c) - getVal(r1 - 1, c)) - target]
                    prefix[(getVal(r2, c) - getVal(r1 - 1, c))] += 1
        
        
        return ans
                
        