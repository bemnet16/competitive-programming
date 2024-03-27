class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        
        for i in range(len(s) - 1, -1, -1):
            
            if s[i] == " " and length >= 1:
                return length
            
            elif s[i] != " ":
                length += 1
        
        
        return length