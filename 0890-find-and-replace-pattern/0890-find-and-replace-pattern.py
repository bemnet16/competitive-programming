class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        def isPermutation(word):
            
            if len(word) != len(pattern):
                return False
            
            word_to_pattern = {}
            pattern_to_word = {}
            
            for char, patt in zip(word, pattern):
                
                if char in word_to_pattern and word_to_pattern[char] != patt:
                    return False
                if patt in pattern_to_word and pattern_to_word[patt] != char:
                    return False
                
                word_to_pattern[char] = patt
                pattern_to_word[patt] = char
            
            return True
                
        
        
        
        ans = []
        
        for word in words:
            if isPermutation(word):
                ans.append(word)
        
        
        return ans
        