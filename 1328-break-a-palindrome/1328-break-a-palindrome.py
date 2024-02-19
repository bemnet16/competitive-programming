class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        # there is no way to break a palindrome of single character 
        if len(palindrome) == 1:
            return ""
        
        idx = -1
        left_a = 0
        for i,char in enumerate(palindrome):
            
            if char == 'a':
                left_a += 1
             
            # there is a character other than 'a'
            if ord(char) > 97:
                idx = i
                break
         
        
        # if all characters are only 'a' idx will be -1
        if idx == -1:
            return palindrome[:(len(palindrome) - 1)] + 'b'
        
        
        right_a = 0
        for i in range(idx,len(palindrome)):
            if palindrome[i] == 'a':
                right_a += 1
        
        # check if only a singel character is between in all 'a's
        if left_a == right_a and palindrome[idx + 1] == 'a':
            idx = palindrome.rindex('a')
            return palindrome[:idx] + 'b' + palindrome[(idx + 1):]
        
        # otherwise return the palindrome string after changing the first non 'a' to 'a'
        return palindrome[:idx] + 'a' + palindrome[(idx + 1):]
            
            
            