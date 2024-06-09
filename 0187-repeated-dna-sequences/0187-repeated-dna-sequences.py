class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        repeated = set()
        occurence = set()
        
        
        for i in range(len(s) - 9):
            
            subString = s[i: i + 10]
            
            if subString in occurence:
                repeated.add(subString)
                
            else:
                occurence.add(subString)
        
        
        return repeated
        
        
        