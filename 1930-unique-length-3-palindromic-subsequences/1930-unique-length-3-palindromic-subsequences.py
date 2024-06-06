class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        indices = defaultdict(list)
        for i, char in enumerate(s):
            if char not in indices:
                indices[char] = [i, i]
            indices[char][1] = i
        
        
        ans = 0
        for start, end in indices.values():
            
            count = set()
            for i in range(start + 1, end):
                count.add(s[i])
                
                if len(count) >= 26:
                    break
            
            ans += len(count)
        
        
        return ans