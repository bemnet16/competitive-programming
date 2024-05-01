class Solution:
    def findComplement(self, num: int) -> int:
        
        temp = 1
        
        for _ in range(num.bit_length()):
            
            num ^= temp
            temp = temp << 1
        
        
        return num
            
        
        