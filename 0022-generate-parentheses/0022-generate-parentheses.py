class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        Parentheses = ["(", ")"]
        combinations = []
        
        
        def isValidParentheses(parentheses):
            
            stack = []
            
            for par in parentheses:
                
                if par == '(':
                    stack.append(par)
                    
                elif par == ')' and stack:
                    stack.pop()
                    
                elif not stack:
                    return False
                
            return len(stack) == 0
        
        
        
        
        def backtrack(combination):
            
            if len(combination) == (2 * n):
                
                if isValidParentheses(combination):
                    temp = combination.copy()
                    combinations.append("".join(temp))
                return
            
            for par in Parentheses:
                combination.append(par)
                backtrack(combination)
                combination.pop()
            
        
        backtrack([])
        return combinations
                