class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        left = 0
        right = len(text) - 1
        ans = 0
        
        while left <= right:
            
            cur = text[right]
            f = True
            
            count = 0
            
            while left < len(text) and (f):
                count += 1
                if text[left] == cur:
                    if text[left - count + 1: left + 1] == text[right - count + 1: right + 1]:
                        f = False
                        if left <= right - count:
                            ans += 2
                        else:
                            ans += 1
                        right -= count
                
                left += 1
        
        return ans
        