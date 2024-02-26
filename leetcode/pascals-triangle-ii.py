class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]

        # previous pascal's triangle from the current index
        pre_pascal = self.getRow(rowIndex - 1)
        
        # the current /that we are trying to build/ pascal triangle
        cur_pascal = [1]
        
        for i in range(len(pre_pascal) - 1):
            cur_pascal.append(pre_pascal[i] + pre_pascal[i + 1])

        cur_pascal.append(1)
        
        return cur_pascal
        
        

        