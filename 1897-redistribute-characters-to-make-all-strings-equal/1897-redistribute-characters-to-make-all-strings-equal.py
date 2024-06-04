class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        n = len(words)
        
        counter = defaultdict(int)
        
        for word in words:
            for char in word:
                counter[char] += 1
        
        for count in counter.values():
            if count % n:
                return False
        
        return True
        