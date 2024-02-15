class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        num_character = {}
        
        for char in s:
            num_character[char] = num_character.get(char, 0) + 1
            
        answer = 0
        remainOne = False
        
        for char in num_character:
            
            count = num_character[char]
            
            if count % 2 == 0:
                answer += count
            
            else:
                answer += (count - 1)
                remainOne = True
        
        if remainOne:
            return answer + 1
        return answer