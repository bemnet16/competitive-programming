class Solution:
    def minimumLength(self, s: str) -> int:
        
        answer = len(s)
        left = 0
        right = len(s) - 1
        
        while left < right and s[left] == s[right]:
            
            if s[left] == s[right]:
                left += 1
                right -= 1
                
                while left <= right and s[left - 1] == s[left]:
                    left += 1
                
                while left <= right and s[right] == s[right + 1]:
                    right -= 1
            
            answer = min(answer, (right - left + 1))
        
        
        return answer
        