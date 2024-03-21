from collections import OrderedDict
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        vowels = 'aeiou'
        
        
        def check(s):
            
            if "".join(list(s.keys())) in vowels:
                return True
            
            return False
        
            
        charCount = defaultdict(int)
        left = 0
        maxlen = 0
        
        for right, char in enumerate(word):
            
            tempChar = charCount[char]
            del charCount[char]
            charCount[char] = tempChar + 1
            
            if check(charCount):
                if len(charCount) == 5:
                    maxlen = max(maxlen, (right - left + 1))
                else:
                    pass
            
            else:
                charCount = defaultdict(int)
                charCount[char] = 1
                left = right
        
        
        return maxlen
                
            
        