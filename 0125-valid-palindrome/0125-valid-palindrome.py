class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        
        while left <= right:
            
            if not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            
            elif not (s[right].isalpha() or s[right].isdigit()):
                right -= 1
            
            elif s[left].lower() != s[right].lower():
                return False
            
            else:
                left += 1
                right -= 1
        
        return True
            
            
        