class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        hashMap = set()
        
        for i in range(len(s) - k + 1):
            hashMap.add(s[i:i + k])
        
        
        for i in range(1 << k):
            
            bins = bin(i)[2:].zfill(k)
            if bins not in hashMap:
                return False
        
        
        return True
        