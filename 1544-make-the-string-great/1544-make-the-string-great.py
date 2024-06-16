class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            
            if (stack and char.lower() == stack[-1].lower()) and ((char.islower() and stack[-1].isupper()) or (char.isupper() and stack[-1].islower())):
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
            
            
                    
        