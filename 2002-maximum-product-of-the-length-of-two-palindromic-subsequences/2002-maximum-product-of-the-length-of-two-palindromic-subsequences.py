class Solution:
    def maxProduct(self, s: str) -> int:
        
        palindroms = {}
        
        for mask in range(1, 2 ** len(s)):
            
            sequence = []
            for i in range(len(s)):
                if mask & (1 << i):
                    sequence.append(s[i])
            
            if sequence and sequence == sequence[::-1]:
                palindroms[mask] = len(sequence)
            
            
        
        _max = 0
        for m1 in palindroms:
            for m2 in palindroms:
                if (m1 & m2) == 0:
                    _max = max(_max, palindroms[m1] * palindroms[m2])
        
        return _max