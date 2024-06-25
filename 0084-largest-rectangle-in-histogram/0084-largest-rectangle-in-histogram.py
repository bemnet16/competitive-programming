class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(-1)
        
        stack = []
        ans = 0
        
        for i, height in enumerate(heights):
            
            top = None
            while stack and stack[-1][1] > height:
                top = stack.pop()
                ans = max(ans, top[1] * (i - top[0]))
            
            if top:
                stack.append((top[0], height))
            else:
                stack.append((i, height))
        
        return ans
        