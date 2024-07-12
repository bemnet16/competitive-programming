class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        ans = 0
        
        if x >= y:
            s, count = self.count(s, 'a', 'b')
            ans += count * x
            
            s, count = self.count(s, 'b', 'a')
            ans += count * y
        
        else:
            s, count = self.count(s, 'b', 'a')
            ans += count * y
            
            s, count = self.count(s, 'a', 'b')
            ans += count * x
    
        return ans
    
    
    def count(self, s, fir, sec):
        
        stack = []
        count = 0
        
        for char in s:
            if stack and char == sec and stack[-1] == fir:
                stack.pop()
                count += 1
            else:
                stack.append(char)
        
        return "".join(stack), count