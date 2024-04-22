class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        if len(words) <= 1:
            return True
        
        orderDict = {}
        for i, char in enumerate(order):
            orderDict[char] = i
        
        
        for i in range(1, len(words)):
            
            for j in range(len(words[i - 1])):
                
                if j >= len(words[i]):
                    return False
                
                if orderDict[words[i - 1][j]] < orderDict[words[i][j]]:
                    break
                
                if orderDict[words[i - 1][j]] > orderDict[words[i][j]]:
                    return False
                    
              
            
        return True
        
