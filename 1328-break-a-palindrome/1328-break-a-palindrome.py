class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        count_a = 0
        for p in palindrome:
            if p == 'a':
                count_a += 1
        
        if len(palindrome) == 1:
            return ""
        
        idx = -1
        count = 0
        
        for i,char in enumerate(palindrome):
            
            if char == 'a':
                count += 1
                
            if ord(char) > 97:
                idx = i
                break
        
        if idx == -1:
            return palindrome[:(len(palindrome) - 1)] + 'b'
        
        if (count_a - count) == count and palindrome[idx + 1] == 'a':
            idx = palindrome.rindex('a')
            return palindrome[:idx] + 'b' + palindrome[(idx + 1):]
        
        return palindrome[:idx] + 'a' + palindrome[(idx + 1):]
            
            
            