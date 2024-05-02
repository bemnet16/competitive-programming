class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        pre_xor = [nums[0]]
        
        for i in range(1, len(nums)):
            pre_xor.append(pre_xor[-1] ^ nums[i])
        
        
        mx = (2 ** maximumBit) - 1
        
        answer = []
        
        for num in pre_xor:
            
            temp = 1
            k = mx
            
            while k:
                
                temp = (temp << 1) 
                temp ^= ((k ^ num) & 1)
                k = k >> 1
                num = num >> 1
            
            ans = 0
            
            while temp > 1:
                
                ans = ans << 1
                ans ^= (temp & 1)
                temp = temp >> 1
            
            answer.append(ans)
                
                
        
        return answer[::-1]
                
                
                
        