class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(-1)
        
        stack = []
        ans = 0
        
        for i, height in enumerate(heights):
            
            start = i
            while stack and stack[-1][1] > height:
                top = stack.pop()
                start = top[0]
                ans = max(ans, top[1] * (i - top[0]))
            
            stack.append((start, height))
        
        return ans
        