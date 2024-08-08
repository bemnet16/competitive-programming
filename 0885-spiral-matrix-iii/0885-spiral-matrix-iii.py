class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        
        
        ans = [[rStart, cStart]]
        row, col = rStart, cStart
        x, y = 1, 1
        
        
        def addCoordinate(row, col):
            if (0 <= row < rows) and (0 <= col < cols):
                ans.append([row, col])
            
        
        while len(ans) < (rows * cols):
            
            for _ in range(x):
                col += 1
                addCoordinate(row, col)
            x += 1
            
            for _ in range(y):
                row += 1
                addCoordinate(row, col)
            y += 1
            
            for _ in range(x):
                col -= 1
                addCoordinate(row, col)
            x += 1
            
            for _ in range(y):
                row -= 1
                addCoordinate(row, col)
            y += 1
        
        return ans
            
            
            