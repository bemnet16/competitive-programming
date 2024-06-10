class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        removed = set()
        stack = []
        
        for i, char in enumerate(s):
            if char == ')':
                if not stack:
                    removed.add(i)
                else:
                    removed.remove(stack.pop())
            
            elif char == '(':
                stack.append(i)
                removed.add(i)
        
        
        ans = []
        for i, char in enumerate(s):
            if i in removed:
                continue
            ans.append(char)
        
        return "".join(ans)
        