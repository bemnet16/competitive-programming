from collections import deque 

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stk = []
        d = deque()
        
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            
            elif c == "*":
                d.append(i)
            
            elif c == ")" and stk:
                stk.pop()
            
            elif c == ")" and d:
                p = d[0]
                if p < i:
                    d.popleft()
            else:
                return False
        
        while stk and d:
            if stk[-1] < d[-1]:
                stk.pop()
                d.pop()
            else:
                break
        
        return not stk