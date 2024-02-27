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
        
        
        
        
        def backtrack(combination, count_open, count_close):
            
            if len(combination) == (2 * n):
                
                if isValidParentheses(combination):
                    temp = combination.copy()
                    combinations.append("".join(temp))
                return
            
            if count_open > n or count_close > n:
                return
            
            for par in Parentheses:
                
                if par == '(':
                    count_open += 1
                else:
                    count_close += 1
                
                combination.append(par)
                
                backtrack(combination, count_open, count_close)
                
                popped = combination.pop()
                if popped == '(':
                    count_open -= 1
                else:
                    count_close -= 1
                
            
        
        backtrack([], 0, 0)
        return combinations
    
    
    
    
    
    
    
    
    
    
                