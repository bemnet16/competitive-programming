class Solution:
    def minimumPushes(self, word: str) -> int:
        
        counter = Counter(word)
        counter = sorted(counter.values(), reverse=True)
        
        ans = 0
        for i, freq in enumerate(counter):
            ans += math.ceil((i + 1) / 8) * freq
        
        return ans