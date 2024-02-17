class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif stack:
                last = stack.pop()
                if c == ')' and last != '(':
                    return False
                elif c == '}' and last != '{':
                    return False
                elif c == ']' and last != '[':
                    return False
            else:
                return False
        
        return len(stack) == 0
        