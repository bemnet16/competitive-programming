class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        
        ans = 0
        l = 0
        total_cost = 0
        
        for r in range(len(s)):
            
            total_cost += abs(ord(s[r]) - ord(t[r]))
            
            if total_cost > maxCost:
                total_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            ans = max(ans, (r - l + 1))
        
        
        return ans
            
            