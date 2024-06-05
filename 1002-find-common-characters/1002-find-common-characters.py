class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        counts = Counter(words[0])
        
        for i in range(1, len(words)):
            
            temp = Counter(words[i])
            
            for char in counts:
                counts[char] = min(counts[char], temp[char])
        
        
        answer = []
        for char in counts:
            answer.extend([char] * counts[char])
        
        return answer
        