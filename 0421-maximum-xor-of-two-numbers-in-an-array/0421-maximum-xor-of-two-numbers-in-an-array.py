class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        mask = 0
        answer = 0
        
        for i in range(32, -1, -1):
            
            mask = mask | 1 << i
            
            possibles = set([num & mask for num in nums])
            
            temp = answer | 1 << i
            
            for possible in possibles:
                
                if possible ^ temp in possibles:
                    answer = temp
                    break
        
        
        return answer
        