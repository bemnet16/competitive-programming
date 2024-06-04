class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        indices = {}
        
        for i, c in enumerate(s):
            
            if c not in indices:
                indices[c] = [i, i]
            
            indices[c][1] = i
        
        ans = -1
        for start, end in indices.values():
            ans = max(ans, end - start - 1)
        
        
        return ans