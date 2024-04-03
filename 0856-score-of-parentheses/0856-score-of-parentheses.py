class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        opening = 0
        isCalculate = True
        score = 0
        
        for par in s:
            
            if par == '(':
                opening += 1
                isCalculate = True
            
            else:
                opening -= 1
                
                if isCalculate:
                    score += (2 ** opening)
                    isCalculate = False
        
        
        return score
                