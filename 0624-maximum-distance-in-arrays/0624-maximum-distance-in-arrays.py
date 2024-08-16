class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        ans = max(abs(arrays[0][0] - arrays[1][-1]), abs(arrays[1][0] - arrays[0][-1]))
        till_min = min(arrays[0][0], arrays[1][0])
        till_max = max(arrays[0][-1], arrays[1][-1])
        
        for i in range(2, len(arrays)):
            
            ans = max(ans, abs(arrays[i][0] - till_max), abs(arrays[i][-1] - till_min))
            till_min = min(till_min, arrays[i][0])
            till_max = max(till_max, arrays[i][-1])
        
        
        return ans