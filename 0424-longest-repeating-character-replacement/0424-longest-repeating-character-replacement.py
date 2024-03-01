class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_count = defaultdict(int)
        max_length = 0
        left = 0
        
        for i in range(len(s)):
            
            char_count[s[i]] += 1
            
            width = i - left + 1
            
            if (width - max(char_count.values())) > k:
                
                char_count[s[left]] -= 1
                left += 1
            
            
            max_length = max(max_length, (i - left + 1))
        
        
        
        return max_length
        