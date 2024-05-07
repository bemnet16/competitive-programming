class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        share_letters = []
        
        for word in words:
            letters = 0
            for char in word:
                letters |= 1 << (ord(char) - 97)
            
            share_letters.append(letters)
        
        
        max_value = 0
        
        for i in range(len(words)):
            for j in range(len(words)):
                if not(share_letters[i] & share_letters[j]):
                    max_value = max(max_value, (len(words[i]) * len(words[j])))
        
        
        return max_value