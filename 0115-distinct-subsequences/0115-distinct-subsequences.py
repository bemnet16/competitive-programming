class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        ls, lt = len(s), len(t)
        
        matrix = [[0 for _ in range(ls)] for _ in range(lt)]
        
        
        if s[0] == t[0]:
            matrix[0][0] = 1
        
        for i in range(1, ls):
            matrix[0][i] = matrix[0][i - 1]
            if s[i] == t[0]:
                matrix[0][i] += 1
            
        for row in range(1, lt):
            for col in range(row, ls):
                
                matrix[row][col] = matrix[row][col - 1]
                
                if s[col] == t[row]:
                    matrix[row][col] += matrix[row - 1][col - 1]
        
        
        return matrix[-1][-1]
                    
                
                