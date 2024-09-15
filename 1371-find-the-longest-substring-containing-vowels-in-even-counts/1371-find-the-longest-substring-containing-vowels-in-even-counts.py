class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        char_map = [0] * 26
        char_map[0] = 1
        char_map[4] = 2
        char_map[8] = 4
        char_map[14] = 8
        char_map[20] = 16
        
        mp = [-1] * 32
        
        prefix_XOR = 0
        ans = 0
        
        for i in range(len(s)):
            
            prefix_XOR ^= char_map[ord(s[i]) - ord('a')]
            
            if mp[prefix_XOR] == -1 and prefix_XOR != 0:
                mp[prefix_XOR] = i
            
            ans = max(ans, i - mp[prefix_XOR])
        
        
        return ans