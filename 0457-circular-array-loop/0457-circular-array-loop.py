class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            
            seq = set()
            start = i
            cur_index = i
            direction = "Forward" if nums[i] > 0 else "Backward"
            
            while cur_index not in seq:
                
                if (direction == "Forward" and nums[cur_index] < 0) or (direction == "Backward" and nums[cur_index] > 0):
                    break
                
                seq.add(cur_index)
                cur_index = (cur_index + nums[cur_index]) % len(nums)
            
            
            if cur_index == start and len(seq) > 1:
                return True
        
        
        
        return False
                
                
                    
            
            
            
            
            
            
        