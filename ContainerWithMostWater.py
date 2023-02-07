class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j= 0, len(height) - 1 
        area =0
        for k in range(j, 0, -1):
            if height[i] < height[j]: 
                area = max(area, height[i] * k)
                i += 1
            else: 
                area  = max(area, height[j] * k)
                j -= 1
        return area
