class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]

        arr = self.getRow(rowIndex - 1)
        
        na = [1]
        for i in range(len(arr) - 1):
            na.append(arr[i] + arr[i + 1])

        na.append(1)
        
        return na
        
        

        