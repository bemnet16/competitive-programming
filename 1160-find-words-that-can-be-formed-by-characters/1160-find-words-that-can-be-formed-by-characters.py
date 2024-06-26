class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        counts = Counter(chars)
        
        ans = 0
        for word in words:
            word_count = defaultdict(int)
            for c in word:
                word_count[c] += 1
            
            good = True
            for c, freq in word_count.items():
                if counts[c] < freq:
                    good = False
                    break
            
            if good:
                ans += len(word)
            
        return ans