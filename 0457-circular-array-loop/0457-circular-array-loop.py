class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            
            seq = set()
            start = i
            next_idx = i
            direction = "Forward" if nums[i] > 0 else "Backward"
            
            while next_idx not in seq:
                
                if (direction == "Forward" and nums[next_idx] < 0) or (direction == "Backward" and nums[next_idx] > 0):
                    break
                
                seq.add(next_idx)
                next_idx = (next_idx + nums[next_idx]) % len(nums)
            
            
            if next_idx == start and len(seq) > 1:
                
                return True
        
        
        
        return False
                
                
                    
            
            
            
            
            
            
        