class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = {}
        left = 0
        right = 0
        longest = 0
        
        while right < len(s):
            
            if not s[right] in visited:
                visited[s[right]] = s[right]
                longest = max(longest, (right - left + 1))
                right += 1
            
            else:
                del visited[s[left]]
                left += 1
        
        
        return longest
            
        