class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        idx = 0
        while matrix[idx][-1] < target:
            
            idx += 1
            
            if idx == len(matrix):
                return False
        
        for i in range(len(matrix[0])):
            if matrix[idx][i] == target:
                return True
        
        
        return False