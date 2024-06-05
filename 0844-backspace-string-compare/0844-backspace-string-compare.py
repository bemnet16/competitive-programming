class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack_s, stack_t = [], []
        
        for char_s in s:
            
            if stack_s and char_s == '#':
                stack_s.pop()
            
            elif char_s != '#':
                stack_s.append(char_s)
            
        for char_t in t:
            if stack_t and char_t == '#':
                    stack_t.pop()
            
            elif char_t != "#":
                stack_t.append(char_t)
        
        
        
        return stack_s == stack_t
        