class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        q = set("qwertyuiop")
        a = set("asdfghjkl")
        z = set("zxcvbnm")
        
        ans = []
        
        for word in words:
            
            word_set = set(word.lower())
            if word_set.issubset(q) or word_set.issubset(a) or word_set.issubset(z):
                ans.append(word)
        
        
        return ans
        