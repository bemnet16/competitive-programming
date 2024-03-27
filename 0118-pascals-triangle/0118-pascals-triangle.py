class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
            
        pascals = [[1]]
        
        for i in range(1, numRows):
            
            cur = pascals[-1]
            temp = [1]
            
            for j in range(len(cur) - 1):
                temp.append(cur[j] + cur[j + 1])
                
            temp.append(1)
            pascals.append(temp)
        
        
        return pascals
            
        