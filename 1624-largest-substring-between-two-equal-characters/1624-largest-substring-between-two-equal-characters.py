class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        indices = {}
        ans = -1
        
        for i, c in enumerate(s):
            
            if c not in indices:
                indices[c] = i
            
            ans = max(ans, i - indices[c] - 1)
        
        return ans