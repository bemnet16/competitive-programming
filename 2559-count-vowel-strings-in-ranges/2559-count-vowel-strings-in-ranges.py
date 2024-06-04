class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix = [0]
        
        for word in words:
            check = word[0] in vowels and word[-1] in vowels
            prefix.append(prefix[-1] + int(check))
        
        
        answer = []
        for l, r in queries:
            answer.append(prefix[r + 1] - prefix[l])
        
        
        return answer