class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        answer = set()
        occurence = set()
        occurence.add(s[:10])
        
        
        for i in range(1, len(s) - 9):
            
            subString = s[i: i + 10]
            
            if subString in occurence:
                answer.add(subString)
                
            else:
                occurence.add(subString)
        
        
        return answer
        
        
        