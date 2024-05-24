class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort()

        cur = ""
        ans = ""
        
        for i, word in enumerate(words):
            
            if cur == word[0:len(word) - 1]:
                if len(word) > len(ans):
                    ans = word
                cur = word
            
            elif cur.startswith(word[:len(word) - 1]):
                cur = word
            
            if len(word) == 1:
                    cur = word
        
        return ans