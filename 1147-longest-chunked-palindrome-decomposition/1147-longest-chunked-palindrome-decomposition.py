class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        left = 0
        right = len(text) - 1
        k = 0
        
        while left <= right:
            
            cur = text[right]
            equal_subtext = False  ## check if the subtext is identifcal from both side(left & right)
            length = 0  ## length of the subtext
            
            while left < len(text) and not equal_subtext:
                
                length += 1
                
                if text[left] == cur:
                    
                    if text[left - length + 1: left + 1] == text[right - length + 1: right + 1]:
                        
                        if left <= right - length:
                            k += 2

                        else:
                            k += 1
                        
                        equal_subtext = True
                        right -= length
                
                left += 1
        
        
        
        return k
        