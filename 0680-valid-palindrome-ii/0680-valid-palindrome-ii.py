class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1
        isTwo = None
        
        while left < right:
            
            if s[left] == s[right]:
                left += 1
                right -= 1
            
            else:
                return (s[left: right] == s[left: right][::-1]) or (s[left + 1: right + 1] == s[left + 1:right + 1][::-1])
        
        
        return True